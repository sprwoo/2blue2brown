from flask import Blueprint, jsonify, request
from app.services.supabase import post_message, get_chat_histories, create_new_session
from app.controllers import Chunky, build_graph
import os
import time
import base64
from .blawb import SupabaseStorage

chat_bp = Blueprint("chat", __name__)
@chat_bp.route("/create_new_session", methods=["POST"])
def route_send_message():
    result = create_new_session()
    return jsonify(result), 200

@chat_bp.route("/get_chat_histories", methods=["GET"])
def route_chat_histories():
    chat_session_id = request.args.get("chat_session_id")
    if not chat_session_id:
        return jsonify({"error": "Missing chat_session_id parameter"}), 400

    try:
        result = get_chat_histories(chat_session_id)
        # for row in result:
        #     print(row)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@chat_bp.route("/chat", methods=["POST"])
def handle_chat():
    from app.controllers import build_graph
    from app.controllers.combiner import CombinedCodeGenerator
    from app.controllers.video_maker import VideoMaker
    user_input = request.form.get("user_input")
    session_id = request.form.get("session_id")

    print("session_id:", session_id)
    print("user_input:", user_input)

    image_summary = None
    image_url = None
    
    if "image" in request.files:
        image_file = request.files["image"]
        if image_file.filename != "":
            chunky = Chunky()
            file_bytes = image_file.read()
            encoded_image = base64.b64encode(file_bytes).decode('utf-8')
            image_summary = chunky.advanced_image_handling(user_input, encoded_image)
            user_input += f"\n\nThe user also uploaded an image with these contents:\n\n{image_summary}"
            
            # Save the image to a temporary location
            temp_dir = "/tmp"
            temp_path = os.path.join(temp_dir, image_file.filename)
            with open(temp_path, "wb") as temp_file:
                temp_file.write(file_bytes)
                
            # Upload the image to Supabase
            storage = SupabaseStorage()
            try:
               image_url = storage.upload_file(temp_path)
            except Exception as e:
               print("Error uploading image:", e)
               image_url = None
            

    graph = build_graph()
    state = {
        "user_input": user_input,
        "session_id": session_id,
    }
    result = graph.invoke(state)
    chat_session_id = session_id
    manim_code = "\n".join(result.get("code_chunks", [])) or None
    
    video_url = None

    if manim_code:
        print(1)
        combiner = CombinedCodeGenerator(result.get("code_chunks"))
        print(2)
        combined_file = combiner.save_to_file(folder="generated_manin", filename='manim.py')
        print(3)
        print(f"Combined Manim script to saved to: {combined_file}")
        print(4)
        
        video_maker = VideoMaker(
            script_file=combined_file,
            scene_name=f"LSTMScene{int(time.time())}",
            quality='l',
            preview=False
        )

        print(5)

        video_maker.render_video()
        print(6)

        print("Video rendering complete. Check the media folder for the output MP4.")
        print(7)

        video_file = os.path.join("media", "videos", "manim", "480p15", f"qdws{int(time.time())}.mp4")
        print(8)

        storage = SupabaseStorage()
        print(9)

        try:
            print("Uploading video... named: ", video_file)
            video_url = storage.upload_file(video_file)
        except Exception as e:
            print("Error uploading video: ", e)
            video_url = None
        print(10)

    # Save the user message
    post_status = post_message("user", user_input, chat_session_id, image_url=image_url)
    print(11)

    ai_message = result.get("chat_response")
    print(12)
    
    post_status = post_message(
       "ai",
       ai_message,
       chat_session_id,
       manim_code=manim_code,
       image_summary=image_summary,
       video_url=video_url
    )

    print(13)

    return jsonify(post_status), 200
from flask import jsonify, request, Blueprint

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload_image", methods=["POST"])
def route_upload_image():
    if "image" not in request.files:
        return jsonify({"error": "No file part named 'image' in request"}), 400

    image_file = request.files["image"]

    if image_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_bytes = image_file.read() # Hetul this is the raw bytes to store as blob

    print("File received:")
    print(f"Filename: {image_file.filename}")
    print(f"Content type: {image_file.content_type}")
    print(f"Size: {len(file_bytes)} bytes")

    return jsonify({"message": "File uploaded successfully", "filename": image_file.filename}), 200

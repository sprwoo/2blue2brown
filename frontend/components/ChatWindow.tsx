"use client";

import React, { useState, useRef, useEffect, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Send, User, Bot, X } from "lucide-react";
import Image from "next/image";
import ReactMarkdown from "react-markdown";
import { Session, Message } from "@/lib/types";

const sendMessageToBackend = async (message: Message): Promise<void> => {
  console.log("Sending message to backend...");
  const formData = new FormData();
  formData.append("session_id", message.session_id || "NULL");
  formData.append("sender", message.sender || "user");
  formData.append("user_input", message.message || "");
  formData.append("image_url", message.imageUrl || "");
  formData.append("image_summary", message.imageSummary || "");
  formData.append("time_created", message.time_created || "");

  if (message.file) {
    formData.append("file", message.file);
  }

  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat`,
      {
        method: "POST",
        body: formData,
      }
    );

    const result = await response.json();
    console.log("Upload response in sendMessageToBackend:", result);

    return result;
  } catch (error) {
    console.error("Upload failed in sendMessageToBackend:", error);
  }
};

export default function ChatWindow({
  user,
  currentSession,
  setCurrentSession,
  messageHistory,
  setMessageHistory,
  newSession,
  setNewSession,
}: {
  user: string;
  currentSession: Session | null;
  setCurrentSession: React.Dispatch<React.SetStateAction<Session | null>>;
  messageHistory: Message[];
  setMessageHistory: React.Dispatch<React.SetStateAction<Message[]>>;
  newSession: boolean;
  setNewSession: React.Dispatch<React.SetStateAction<boolean>>;
}) {
  const [input, setInput] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [dragActive, setDragActive] = useState(false);
  const [videoUrl, setVideoUrl] = useState(null);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const fetchLatestSession = async () => {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_latest_session`
      );
      const latestSession = await response.json();
      setCurrentSession(latestSession);
    };
    fetchLatestSession();
  }, []);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messageHistory]);

  // useEffect(() => {
  //   console.log("currentSession", currentSession);
  //   console.log("chatHistory", messageHistory);
  // });

  useEffect(() => {
    if (newSession) {
      setMessageHistory([]);
      setInput("");
      setFile(null);
      setPreviewUrl(null);
    }
  }, [newSession, setNewSession]);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const droppedFile = acceptedFiles[0];
    if (!droppedFile) return;

    setFile(droppedFile);
    setPreviewUrl(URL.createObjectURL(droppedFile));
    setDragActive(false);
  }, []);

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    multiple: true,
    noClick: true,
    accept: {
      "image/*": [".png", ".jpg", ".jpeg"],
      "application/pdf": [".pdf"],
    },
    onDragEnter: () => setDragActive(true),
    onDragLeave: () => setDragActive(false),
  });

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    setPreviewUrl(URL.createObjectURL(selectedFile));
  };

  const handleSend = async () => {
    if (!input.trim() && !file) return;
    const newMessage: Message = {
      id: null,
      session_id: currentSession?.id || null,
      sender: "user",
      message: input,
      file,
      imageUrl:
        file && file.type.startsWith("image/") ? previewUrl! : undefined,
      time_created: new Date().toISOString(),
    };

    setMessageHistory((prev) => [...prev, newMessage]);
    setInput("");
    setFile(null);
    setPreviewUrl(null);

    console.log("history", messageHistory);
    // setTimeout(() => {
    //   setMessageHistory((prev) => [...prev, aiResponse]);
    // }, 1000);

    const response = await sendMessageToBackend(newMessage);
    const aiMessage = response.message;
    const videoUrl = response.video_url;

    const newMessages: Message[] = [
      {
        id: null,
        session_id: currentSession?.id || null,
        sender: "ai",
        message: aiMessage,
        file: null,
        imageUrl: null,
        time_created: new Date().toISOString(),
      },
    ];

    if (videoUrl) {
      newMessages.push({
        id: null,
        session_id: currentSession?.id || null,
        sender: "ai",
        message: `<video controls class="rounded w-full max-w-md mt-2"><source src="${videoUrl}" type="video/mp4">Your browser does not support the video tag.</video>`,
        file: null,
        imageUrl: null,
        time_created: new Date().toISOString(),
      });
    }

    setMessageHistory((prev) => [...prev, ...newMessages]);

    console.log("history after", messageHistory);
  };

  return (
    <div className="flex flex-col max-w-[1200px] bg-zinc-950">
      <div className="border-b border-zinc-800 p-4 h-17.25 text-sm font-semibold text-zinc-200">
        <div>{currentSession?.title}</div>
        <div>{currentSession?.time_created}</div>
      </div>
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-6">
        {!newSession &&
          messageHistory.map((msg, idx) => {
            return (
              <div key={idx} className="flex items-start gap-4 w-full">
                <div className="mt-1">
                  {msg.sender === "user" ? (
                    <User className="h-5 w-5 text-zinc-400" />
                  ) : (
                    <Bot className="h-5 w-5 text-green-400" />
                  )}
                </div>
                <div
                  className={`flex-1 px-4 py-3 text-[15px] leading-relaxed break-words rounded overflow-x-hidden ${
                    msg.sender === "user"
                      ? "bg-zinc-800 text-zinc-100"
                      : "bg-zinc-900 text-zinc-100"
                  }`}
                >
                  <div
                    className="prose prose-invert max-w-none"
                    dangerouslySetInnerHTML={{ __html: msg.message }}
                  />

                  {msg.imageUrl && (
                    <div className="mt-3">
                      <Image
                        src={msg.imageUrl}
                        alt="Uploaded"
                        width={200}
                        height={200}
                        className="rounded-md"
                      />
                    </div>
                  )}

                  {msg.file &&
                    msg.file.type === "application/pdf" &&
                    !msg.imageUrl && (
                      <div className="mt-3 text-sm text-blue-400 underline">
                        {msg.file.name}
                      </div>
                    )}
                </div>
              </div>
            );
          })}
        <div ref={scrollRef} />
      </div>

      <div
        {...getRootProps()}
        className={`border-t border-zinc-800 p-4 relative ${
          dragActive ? "border-2 border-dashed border-blue-400 bg-zinc-900" : ""
        }`}
      >
        <input {...getInputProps()} />
        {dragActive && (
          <div className="absolute inset-0 flex items-center justify-center text-sm text-blue-400 font-medium z-10 pointer-events-none">
            Drop your image or PDF here
          </div>
        )}

        {previewUrl && (
          <div className="mb-2 flex items-center gap-4 bg-zinc-800 px-4 py-2 rounded">
            {file?.type.startsWith("image/") ? (
              <Image
                src={previewUrl}
                alt="Preview"
                width={80}
                height={80}
                className="rounded object-cover"
              />
            ) : (
              <div className="text-sm text-zinc-100 flex-1 truncate">
                {file?.name}
              </div>
            )}
            <Button
              variant="ghost"
              size="icon"
              onClick={(e) => {
                e.stopPropagation();
                setFile(null);
                setPreviewUrl(null);
              }}
            >
              <X className="h-4 w-4" />
            </Button>
          </div>
        )}

        <div className="flex items-center justify-between gap-2 w-[1150px]">
          <Textarea
            placeholder="Type your message or drag a file..."
            className="flex-1 resize-none h-10"
            rows={1}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                setNewSession(false);
                handleSend();
              }
            }}
          />
          <input
            type="file"
            ref={fileInputRef}
            accept="image/*,application/pdf"
            onChange={handleFileSelect}
            className="hidden"
          />

          <Button
            className="h-[62px] cursor-pointer px-4"
            onClick={() => fileInputRef.current?.click()}
          >
            Choose File
          </Button>
          <Button
            className="h-[62px] cursor-pointer px-4"
            onClick={async () => {
              if (!file) return;

              const formData = new FormData();
              formData.append("image", file);
              formData.append(
                "session_id",
                "1828e6f9-707d-4d04-b5e5-5d036698b9d6"
              );
              formData.append("user_input", input);

              try {
                const response = await fetch(
                  `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/chat`,
                  {
                    method: "POST",
                    body: formData,
                  }
                );

                const result = await response.json();
                console.log("Upload response in ChatWindow:", result);
              } catch (error) {
                console.error("Upload failed in ChatWindow:", error);
              }
            }}
          >
            Upload
          </Button>

          <Button onClick={handleSend} className="h-[62px] cursor-pointer px-4">
            <Send className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}

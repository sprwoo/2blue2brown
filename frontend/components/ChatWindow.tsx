"use client";

import { useState, useRef, useEffect, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Send, User, Bot, X } from "lucide-react";
import Image from "next/image";
import ReactMarkdown from "react-markdown";

type Message = {
  sender: "user" | "ai";
  content: string;
  file?: File | null;
  imageUrl?: string;
};

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "user",
      content: "What is the Pythagorean theorem?",
    },
    {
      sender: "ai",
      content:
        "The Pythagorean theorem states that:\n\n**a² + b² = c²**\n\nWhere *a* and *b* are the legs of a right triangle and *c* is the hypotenuse.",
    },
  ]);
  const [input, setInput] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [dragActive, setDragActive] = useState(false);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

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

  const handleSend = () => {
    if (!input.trim() && !file) return;

    const newMessage: Message = {
      sender: "user",
      content: input,
      file,
      imageUrl:
        file && file.type.startsWith("image/") ? previewUrl! : undefined,
    };

    setMessages((prev) => [...prev, newMessage]);
    setInput("");
    setFile(null);
    setPreviewUrl(null);
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          content:
            "Here's what I found based on your upload:\n\n### Steps to Solve Quadratic\n\n1. Rearrange the equation\n2. Factor if possible\n3. Apply the quadratic formula\n\nLet me know if you'd like a deeper explanation!",
        },
      ]);
    }, 1000);
  };

  return (
    <div className="flex flex-col max-w-[1200px] bg-zinc-950">
      <div className="border-b border-zinc-800 p-4 text-sm font-semibold text-zinc-200">
        AI Chat Session
      </div>
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-6">
        {messages.map((msg, idx) => (
          <div key={idx} className="flex items-start gap-4 w-full">
            <div className="mt-1">
              {msg.sender === "user" ? (
                <User className="h-5 w-5 text-zinc-400" />
              ) : (
                <Bot className="h-5 w-5 text-green-400" />
              )}
            </div>
            <div
              className={`flex-1 px-4 py-3 text-[15px] leading-relaxed break-words overflow-x-hidden ${
                msg.sender === "user"
                  ? "bg-zinc-800 text-zinc-100"
                  : "bg-zinc-900 text-zinc-100"
              }`}
            >
              <ReactMarkdown
                components={{
                  p: ({ node, ...props }) => (
                    <p className="prose prose-invert max-w-none" {...props} />
                  ),
                }}
              >
                {msg.content}
              </ReactMarkdown>

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
        ))}
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

        {/* Input and Send */}
        <div className="flex items-center gap-2">
          <Textarea
            placeholder="Type your message or drag a file..."
            className="flex-1 resize-none h-10"
            rows={1}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleSend();
              }
            }}
          />
          <Button onClick={handleSend} className="h-10 px-4">
            <Send className="h-4 w-4" />
          </Button>
        </div>
      </div>
    </div>
  );
}

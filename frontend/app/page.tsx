"use client"

import type React from "react"

import { useState, useEffect, useRef } from "react"
import { v4 as uuidv4 } from "uuid"
import { format } from "date-fns"
import { motion, AnimatePresence } from "framer-motion"
import { PlusIcon, SendIcon, PaperclipIcon, Loader2 } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { ThemeToggle } from "@/components/theme-toggle"
import { cn } from "@/lib/utils"
import ReactMarkdown from "react-markdown"

// Types
interface Message {
  id: string
  content: string
  role: "user" | "assistant"
  timestamp: Date
  media?: {
    type: "image" | "video" | "pdf"
    url: string
  }
}

interface ChatSession {
  id: string
  title: string
  messages: Message[]
  createdAt: Date
}

export default function ChatInterface() {
  const [sessions, setSessions] = useState<ChatSession[]>([])
  const [activeSession, setActiveSession] = useState<ChatSession | null>(null)
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  // Add these state variables at the top of the component
  const [isDragging, setIsDragging] = useState(false)
  const [uploadedImage, setUploadedImage] = useState<File | null>(null)
  const [uploadedImagePreview, setUploadedImagePreview] = useState<string | null>(null)

  // Group sessions by date
  const groupedSessions = sessions.reduce(
    (groups, session) => {
      const date = format(session.createdAt, "MMMM d, yyyy")
      if (!groups[date]) {
        groups[date] = []
      }
      groups[date].push(session)
      return groups
    },
    {} as Record<string, ChatSession[]>,
  )

  // Create a new chat session
  const createNewChat = () => {
    const newSession: ChatSession = {
      id: uuidv4(),
      title: "New Chat",
      messages: [],
      createdAt: new Date(),
    }
    setSessions([newSession, ...sessions])
    setActiveSession(newSession)
  }

  // Load a chat session
  const loadSession = (session: ChatSession) => {
    setActiveSession(session)
  }

  // Add these handlers before the return statement
  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(false)
  }

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(false)

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const file = e.dataTransfer.files[0]
      if (file.type.startsWith("image/")) {
        setUploadedImage(file)
        setUploadedImagePreview(URL.createObjectURL(file))
      }
    }
  }

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0]
      if (file.type.startsWith("image/")) {
        setUploadedImage(file)
        setUploadedImagePreview(URL.createObjectURL(file))
      }
    }

    // Reset file input
    if (fileInputRef.current) {
      fileInputRef.current.value = ""
    }
  }

  const clearUploadedImage = () => {
    setUploadedImage(null)
    setUploadedImagePreview(null)
  }

  // Send a message
  const sendMessage = async () => {
    if (!input.trim() || !activeSession) return

    setIsLoading(true)

    // Create user message
    const userMessage: Message = {
      id: uuidv4(),
      content: input,
      role: "user",
      timestamp: new Date(),
    }

    // Add this to the sendMessage function, after creating the userMessage
    if (uploadedImage && uploadedImagePreview) {
      userMessage.media = {
        type: "image",
        url: uploadedImagePreview,
      }

      // Clear the uploaded image after sending
      clearUploadedImage()
    }

    // Update session with user message
    const updatedSession = {
      ...activeSession,
      messages: [...activeSession.messages, userMessage],
    }

    // Update sessions state
    setSessions(sessions.map((s) => (s.id === activeSession.id ? updatedSession : s)))
    setActiveSession(updatedSession)
    setInput("")

    // Simulate AI response after a delay
    setTimeout(() => {
      const aiMessage: Message = {
        id: uuidv4(),
        content:
          "This is a simulated response from the AI assistant. It supports **markdown** formatting including:\n\n- Bullet points\n- *Italic text*\n- [Links](https://nextjs.org)\n\n```javascript\n// And code blocks\nconst greeting = 'Hello world!';\nconsole.log(greeting);\n```",
        role: "assistant",
        timestamp: new Date(),
      }

      // Update session with AI message
      const finalSession = {
        ...updatedSession,
        messages: [...updatedSession.messages, aiMessage],
        title: updatedSession.title === "New Chat" ? userMessage.content.slice(0, 30) : updatedSession.title,
      }

      // Update sessions state
      setSessions(sessions.map((s) => (s.id === activeSession.id ? finalSession : s)))
      setActiveSession(finalSession)
      setIsLoading(false)
    }, 1500)
  }

  // Handle file upload
  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0] && activeSession) {
      const file = e.target.files[0]
      const fileType = file.type.startsWith("image/") ? "image" : file.type.startsWith("video/") ? "video" : "pdf"

      const reader = new FileReader()
      reader.onload = (event) => {
        if (event.target?.result) {
          // Create user message with media
          const userMessage: Message = {
            id: uuidv4(),
            content: `Uploaded a ${fileType}`,
            role: "user",
            timestamp: new Date(),
            media: {
              type: fileType as "image" | "video" | "pdf",
              url: event.target.result as string,
            },
          }

          // Update session with user message
          const updatedSession = {
            ...activeSession,
            messages: [...activeSession.messages, userMessage],
          }

          // Update sessions state
          setSessions(sessions.map((s) => (s.id === activeSession.id ? updatedSession : s)))
          setActiveSession(updatedSession)

          // Simulate AI response after a delay
          setIsLoading(true)
          setTimeout(() => {
            const aiMessage: Message = {
              id: uuidv4(),
              content: `I've received your ${fileType}. What would you like to know about it?`,
              role: "assistant",
              timestamp: new Date(),
            }

            // Update session with AI message
            const finalSession = {
              ...updatedSession,
              messages: [...updatedSession.messages, aiMessage],
              title:
                updatedSession.title === "New Chat"
                  ? `${fileType.charAt(0).toUpperCase() + fileType.slice(1)} Chat`
                  : updatedSession.title,
            }

            // Update sessions state
            setSessions(sessions.map((s) => (s.id === activeSession.id ? finalSession : s)))
            setActiveSession(finalSession)
            setIsLoading(false)
          }, 1500)
        }
      }
      reader.readAsDataURL(file)
    }

    // Reset file input
    if (fileInputRef.current) {
      fileInputRef.current.value = ""
    }
  }

  // Handle textarea height
  const adjustTextareaHeight = () => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto"
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`
    }
  }

  // Scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [activeSession?.messages])

  // Initialize with a default session
  useEffect(() => {
    if (sessions.length === 0) {
      createNewChat()
    }
  }, [sessions.length])

  // Handle textarea input
  useEffect(() => {
    adjustTextareaHeight()
  }, [input])
  return (
    <div className="flex h-screen w-screen overflow-hidden bg-zinc-50 text-zinc-900 dark:bg-slate-900 dark:text-slate-100">
      {/* Sidebar */}
      <div className="w-72 h-full border-r border-zinc-200 dark:border-slate-700 bg-zinc-50 dark:bg-slate-900 flex flex-col">
        <div className="p-4">
          <Button
            onClick={createNewChat}
            className="w-full bg-zinc-900 hover:bg-zinc-800 text-white dark:bg-slate-700 dark:hover:bg-slate-600 flex items-center justify-center gap-2"
          >
            <PlusIcon className="h-4 w-4" />
            <span>New Chat</span>
          </Button>
        </div>

        <div className="flex-1 overflow-y-auto p-2">
          {Object.entries(groupedSessions).map(([date, dateSessions]) => (
            <div key={date} className="mb-4">
              <h3 className="text-xs text-zinc-500 dark:text-slate-400 px-2 mb-2">{date}</h3>
              {dateSessions.map((session) => (
                <button
                  key={session.id}
                  onClick={() => loadSession(session)}
                  className={cn(
                    "w-full text-left px-3 py-2 rounded-md mb-1 text-sm transition-colors",
                    activeSession?.id === session.id
                      ? "bg-zinc-200 dark:bg-slate-700"
                      : "hover:bg-zinc-100 dark:hover:bg-slate-800",
                  )}
                >
                  {session.title}
                </button>
              ))}
            </div>
          ))}
        </div>
      </div>

      {/* Main Chat Window */}
      <div className="flex-1 flex flex-col h-full">
        {/* Header */}
        <header className="h-14 border-b border-zinc-200 dark:border-slate-700 flex items-center justify-between px-4">
          <h1 className="font-semibold">AI Chat Assistant</h1>
          <ThemeToggle />
        </header>

        {/* Messages Area */}
        <div className="flex-1 overflow-y-auto pb-4">
          {activeSession && activeSession.messages.length > 0 ? (
            <div className="max-w-3xl mx-auto">
              <AnimatePresence>
                {activeSession.messages.map((message) => (
                  <motion.div
                    key={message.id}
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.3 }}
                    className={cn(
                      "py-6 px-4 md:px-8",
                      message.role === "assistant" ? "bg-zinc-100 dark:bg-slate-800" : ""
                    )}
                  >
                    <div className="max-w-3xl mx-auto flex">
                      <div
                        className={cn(
                          "prose dark:prose-invert prose-zinc dark:prose-slate max-w-none",
                          message.role === "user" ? "ml-auto" : ""
                        )}                        
                      >
                        {message.media ? (
                          <div className="mb-2">
                            {message.media.type === "image" && (
                              // eslint-disable-next-line @next/next/no-img-element
                              <img
                                src={message.media.url || "/placeholder.svg"}
                                alt="User uploaded image"
                                className="max-h-96 rounded-md"
                              />
                            )}
                            {message.media.type === "video" && (
                              <video src={message.media.url} controls className="max-h-96 rounded-md" />
                            )}
                            {message.media.type === "pdf" && (
                              <div className="flex items-center gap-2 p-4 border border-zinc-200 dark:border-slate-700 rounded-md">
                                <span>PDF Document</span>
                                <a
                                  href={message.media.url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="text-blue-600 dark:text-blue-400 underline"
                                >
                                  View PDF
                                </a>
                              </div>
                            )}
                          </div>
                        ) : (
                          <ReactMarkdown>{message.content}</ReactMarkdown>
                        )}
                      </div>
                    </div>
                  </motion.div>
                ))}
              </AnimatePresence>
              <div ref={messagesEndRef} className="h-4" />
            </div>
          ) : (
            <div className="h-full flex items-center justify-center">
              <div className="text-center max-w-md">
                <h2 className="text-2xl font-bold mb-2">Welcome to AI Chat</h2>
                <p className="text-zinc-600 dark:text-slate-400">
                  Start a new conversation or select an existing chat from the sidebar.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div
          className="sticky bottom-0 bg-zinc-50 dark:bg-slate-900 border-t border-zinc-200 dark:border-slate-700 p-4 pt-2"
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <div className="max-w-3xl mx-auto">
            <div
              className={cn(
                "relative border-2 rounded-md transition-all",
                isDragging
                  ? "border-dashed border-indigo-500 bg-zinc-100/50 dark:bg-slate-800/50"
                  : "border-zinc-300 dark:border-slate-600",
              )}
            >
              {isDragging && (
                <div className="absolute inset-0 flex items-center justify-center bg-zinc-50/90 dark:bg-slate-900/90 rounded-md z-10">
                  <p className="text-indigo-600 dark:text-indigo-400 font-medium">Drop image here</p>
                </div>
              )}

              {/* Image Preview */}
              {uploadedImagePreview && (
                <div className="p-2 border-b border-zinc-200 dark:border-slate-700">
                  <div className="flex items-center gap-2">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img
                      src={uploadedImagePreview || "/placeholder.svg"}
                      alt="Upload preview"
                      className="h-16 w-16 rounded-md object-cover"
                    />
                    <Button variant="ghost" size="icon" onClick={clearUploadedImage} className="h-6 w-6">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-4 w-4"
                      >
                        <path d="M18 6 6 18"></path>
                        <path d="m6 6 12 12"></path>
                      </svg>
                    </Button>
                    <span className="text-sm text-zinc-500 dark:text-slate-400">{uploadedImage?.name}</span>
                  </div>
                </div>
              )}

              <div className="flex items-end gap-2 p-2">
                <input
                  type="file"
                  accept="image/*,video/*,application/pdf"
                  className="hidden"
                  ref={fileInputRef}
                  onChange={handleFileSelect}
                />
                <Button
                  variant="ghost"
                  size="icon"
                  className="h-8 w-8 rounded-md flex-shrink-0"
                  onClick={() => fileInputRef.current?.click()}
                >
                  <PaperclipIcon className="h-5 w-5" />
                </Button>
                <Textarea
                  ref={textareaRef}
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Message AI..."
                  className="min-h-10 resize-none border-0 focus-visible:ring-0 focus-visible:ring-offset-0 px-4 py-2 text-sm"
                  onKeyDown={(e) => {
                    if (e.key === "Enter" && !e.shiftKey) {
                      e.preventDefault()
                      sendMessage()
                    }
                  }}
                />
                <Button
                  onClick={sendMessage}
                  disabled={(!input.trim() && !uploadedImage) || isLoading || !activeSession}
                  className="h-8 w-8 rounded-md flex-shrink-0"
                  size="icon"
                >
                  {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <SendIcon className="h-4 w-4" />}
                </Button>
              </div>
            </div>
            <div className="text-xs text-center mt-2 text-zinc-500 dark:text-slate-400">
              Press Enter to send, Shift+Enter for a new line
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}


"use client";

import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Session, Message } from "@/lib/types";
import { Plus } from "lucide-react";
import React, { useState, useEffect } from "react";

export default function Sidebar({
  user,
  currentSession,
  setCurrentSession,
  messageHistory,
  setMessageHistory,
  sessionsList,
  setSessionsList,
  newSession,
  setNewSession,
}: {
  user: string;
  currentSession: Session | null;
  setCurrentSession: React.Dispatch<React.SetStateAction<Session | null>>;
  messageHistory: Message[];
  setMessageHistory: React.Dispatch<React.SetStateAction<Message[]>>;
  sessionsList: Session[];
  setSessionsList: React.Dispatch<React.SetStateAction<Session[]>>;
  newSession: boolean;
  setNewSession: React.Dispatch<React.SetStateAction<boolean>>;
}) {
  useEffect(() => {
    const getSessions = async () => {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_all_chat_sessions`
      );
      const results = await response.json();
      setSessionsList(results);
    };
    getSessions();
  }, []);

  useEffect(() => console.log("sessions", sessionsList));
  const handleSession = async (id: string) => {
    const session_response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_chat_session?uuid=${id}`
    );
    const session_result = await session_response.json();
    console.log("current session: ", session_result);

    const history_response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_chat_histories?chat_session_id=${id}`
    );
    const history_result = await history_response.json();
    console.log("history: ", history_result);

    setCurrentSession(session_result);
    setMessageHistory(history_result);
  };

  return (
    <div className="w-64 bg-zinc-900 border-r border-zinc-700 flex flex-col">
      <div className="p-4 border-b border-zinc-700">
        <Button
          className="w-full cursor-pointer flex gap-2 bg-zinc-800 text-zinc-100 hover:bg-zinc-700 transition-colors duration-200"
          variant="secondary"
          onClick={() => {
            setNewSession(true); // Make a new session
          }}
        >
          <Plus className="mr-2 h-4 w-4" />
          New Chat
        </Button>
      </div>
      <ScrollArea className="flex-1">
        <div className="p-4 space-y-2">
          {sessionsList.length > 0 &&
            sessionsList?.map((session, index) => (
              <div
                key={`${session.id}-${index}`}
                className="p-3 rounded-lg bg-zinc-800 hover:bg-zinc-700 cursor-pointer"
                onClick={() => setCurrentSession(session)}
              >
                <div className="text-sm font-medium">{session.title}</div>
                <div className="text-xs text-zinc-400">
                  {session.time_created}
                </div>
              </div>
            ))}
        </div>
      </ScrollArea>
    </div>
  );
}

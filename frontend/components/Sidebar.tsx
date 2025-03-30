"use client";

import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Session } from "@/lib/types";
import { Plus } from "lucide-react";
import React, { useState, useEffect } from "react";

export default function Sidebar({
  user,
  session,
  setSession,
  sessions,
  setSessions,
}: {
  user: string;
  session: Session | null;
  setSession: React.Dispatch<React.SetStateAction<Session | null>>;
  sessions: Session[];
  setSessions: React.Dispatch<React.SetStateAction<Session[]>>;
}) {
  useEffect(() => {
    const getSessions = async () => {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_all_chat_sessions`
      );
      const results = await response.json();
      setSessions(results);
    };
    getSessions();
  }, []);

  useEffect(() => console.log("sessions", sessions));
  const handleSession = async (id: string) => {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/get_chat_session?uuid=${id}`
    );
    const result = await response.json();
    setSession(result);
  };

  return (
    <div className="w-64 bg-zinc-900 border-r border-zinc-700 flex flex-col">
      <div className="p-4 border-b border-zinc-700">
        <Button
          className="w-full cursor-pointer flex gap-2 bg-zinc-800 text-zinc-100 hover:bg-zinc-700 transition-colors duration-200"
          variant="secondary"
          // onClick={() => setSession("New session")}
        >
          <Plus className="mr-2 h-4 w-4" />
          New Chat
        </Button>
      </div>
      <ScrollArea className="flex-1">
        <div className="p-4 space-y-2">
          {sessions.length > 0 && sessions?.map((session, index) => (
            <div
              key={`${session.id}-${index}`}
              className="p-3 rounded-lg bg-zinc-800 hover:bg-zinc-700 cursor-pointer"
              onClick={() => handleSession(session.id)}
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

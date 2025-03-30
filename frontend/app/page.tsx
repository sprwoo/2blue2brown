"use client";

import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import { useState, useEffect } from "react";
import { Session } from "@/lib/types";

export default function Home() {
  const [user, setUser] = useState<string>("Broski");
  const [sessions, setSessions] = useState<Session[]>([]);
  const [session, setSession] = useState<Session | null>(null);

  return (
    <main className="flex h-screen">
      <Sidebar
        user={user}
        session={session}
        setSession={setSession}
        sessions={sessions}
        setSessions={setSessions}
      />
      <ChatWindow user={user} session={session} setSession={setSession} />
    </main>
  );
}

"use client";

import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import { useState } from "react";

export default function Home() {
  const [user, setUser] = useState<string>("Broski");
  // we'll change these states later probably
  const [session, setSession] = useState<string>("Session 1")
  return (
    <main className="flex h-screen">
      <Sidebar user={user} session={session} setSession={setSession}/>
      <ChatWindow user={user} session={session} />
    </main>
  );
}

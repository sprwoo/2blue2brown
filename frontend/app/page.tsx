"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";
import { Session } from "@/lib/types";
import { supabase } from "@/lib/supabaseClient";

export default function Home() {
  const router = useRouter();
  const [user, setUser] = useState<string>("Broski");
  const [sessions, setSessions] = useState<Session[]>([]);
  const [session, setSession] = useState<Session | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      const { data } = await supabase.auth.getSession();
      if (!data.session) {
        router.push("/login");
      } else {
        setUser(data.session.user.email || "User");
        setLoading(false);
      }
    };
    checkAuth();
  }, [router]);

  if (loading) return <div className="p-4">Loading...</div>;

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

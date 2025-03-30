"use client";
import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabaseClient";

export default function AuthCallback() {
  const router = useRouter();

  useEffect(() => {
    const handleAuth = async () => {
      const { data } = await supabase.auth.getSession();
      const token = data?.session?.access_token;
      if (token) {
        localStorage.setItem("token", token);
        router.push("/");
      } else {
        router.push("/login");
      }
    };

    handleAuth();
  }, [router]);

  return <p className="text-center mt-10">Redirecting...</p>;
}

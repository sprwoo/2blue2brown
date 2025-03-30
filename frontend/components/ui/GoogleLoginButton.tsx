"use client";

import { supabase } from "@/lib/supabaseClient";

export default function GoogleLoginButton() {
  const loginWithGoogle = async () => {
    const redirectUrl = `${window.location.origin}/auth`;
    await supabase.auth.signInWithOAuth({
      provider: "google",
      options: {
        redirectTo: redirectUrl,
      },
    });
  };

  return (
    <button
      onClick={loginWithGoogle}
      className="bg-blue-600 cursor-pointer text-white hover:bg-blue-700 px-4 py-2 rounded"
    >
      Login with Google
    </button>
  );
}

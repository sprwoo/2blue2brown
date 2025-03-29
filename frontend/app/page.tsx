import Sidebar from "@/components/Sidebar";
import ChatWindow from "@/components/ChatWindow";

export default function Home() {
  return (
    <main className="flex h-screen">
      <Sidebar />
      <ChatWindow />
    </main>
  );
}

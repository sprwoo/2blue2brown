export interface Session {
    id: string;
    time_created: string;
    title: string;
    user: string;
}

export interface Message {
    id: string | null;
    session_id: string | null;
    sender: "user" | "ai";
    message: string | null;
    imageUrl?: string | null;
    file?: File | null;
    time_created: string | null;
    imageSummary?: string | null;
}

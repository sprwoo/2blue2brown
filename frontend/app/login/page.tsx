import GoogleLoginButton from "@/components/ui/GoogleLoginButton";

export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md text-center space-y-4">
        <h1 className="text-2xl text-black font-bold">Welcome</h1>
        <p className="text-gray-600">Sign in to continue</p>
        <GoogleLoginButton />
      </div>
    </div>
  );
}

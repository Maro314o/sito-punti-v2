"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ArrowLeftIcon } from "lucide-react";
import { useState } from "react";
import { useAuth } from "@/contexts/AuthContext";
import { login as apiLogin, logout as apiLogout } from "@/lib/api";

export default function FormWrapper() {
  const { user, refreshUser } = useAuth();
  const [page, setPage] = useState<"home" | "login" | "register" | "forgot" | "logged">(
    user ? "logged" : "home"
  );

  return (
    <div className="container mx-auto text-center w-auto md:w-xl lg:w-4xl p-10 md:p-15 lg:p-25">
      {page === "logged" ? (
        <LoggedContent 
          nome={user?.nominativo || ""} 
          onLogout={async () => {
            await apiLogout();
            await refreshUser();
            setPage("home");
          }} 
        />
      ) : page === "login" ? (
        <LoginContent
          onBack={() => setPage("home")}
          onRegister={() => setPage("register")}
          onForgotPassword={() => setPage("forgot")}
          onLoginSuccess={async () => {
            await refreshUser();
            setPage("logged");
          }}
        />
      ) : page === "register" ? (
        <RegisterContent onLogin={() => setPage("login")} />
      ) : page === "forgot" ? (
        <ForgotContent onBack={() => setPage("login")} />
      ) : (
        <HomeContent onLogin={() => setPage("login")} />
      )}
    </div>
  );
}

const LoginContent = ({
  onBack,
  onRegister,
  onForgotPassword,
  onLoginSuccess,
}: {
  onBack: () => void;
  onRegister: () => void;
  onForgotPassword: () => void;
  onLoginSuccess: () => void;
}) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const result = await apiLogin(email, password);
      if (result.success) {
        onLoginSuccess();
      } else {
        setError(result.error || "Login fallito");
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login fallito");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleLogin} className="grid grid-col gap-5">
      <Button type="button" variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>

      <div className="grid grid-col gap-2 mx-auto w-auto md:w-md">
        <Input 
          type="email" 
          placeholder="email" 
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <Input 
          type="password" 
          placeholder="password" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      {error && <p className="text-red-500 text-sm">{error}</p>}

      <Button type="button" variant={"link"} onClick={onForgotPassword}>
        Hai dimenticato la password?
      </Button>

      <div>
        <Button type="submit" variant={"outline"} disabled={loading}>
          {loading ? "Accesso in corso..." : "Accedi"}
        </Button>
      </div>

      <Button type="button" variant={"link"} onClick={onRegister}>
        Non hai un account?
        <br />
        Registrati
      </Button>
    </form>
  );
};

const LoggedContent = ({
  nome,
  onLogout,
}: {
  nome: string;
  onLogout: () => void;
}) => {
  return (
    <div className="grid grid-col gap-5">
      <h2>
        Benvenuto, {nome}!
      </h2>
      
      <div>
        <Button variant={"outline"} onClick={onLogout}>
          Logout
        </Button>
      </div>
    </div>
  );
};

const RegisterContent = ({ onLogin }: { onLogin: () => void }) => {
  return (
    <div className="grid grid-col gap-5">
      <div className="grid grid-col gap-2 mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
        <Input type="text" placeholder="cognome" />
        <Input type="text" placeholder="nome" />
        <Input type="password" placeholder="password" />
        <Input type="password" placeholder="conferma password" />
      </div>
      <div>
        <Button variant={"outline"}>Registrati</Button>
      </div>

      <Button variant={"link"} onClick={onLogin}>
        Hai già un account?
        <br />
        Accedi
      </Button>
    </div>
  );
};

const ForgotContent = ({ onBack }: { onBack: () => void }) => {
  return (
    <div className="grid grid-col gap-5">
      <Button type="button" variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>

      <h3>Verrà mandata una mail per il cambio password</h3>
      <div className="mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
      </div>

      <div>
        <Button variant={"outline"}>Invia</Button>
      </div>
    </div>
  );
};

const HomeContent = ({ onLogin }: { onLogin: () => void }) => {
  return (
    <div>
      <Button variant={"outline"} onClick={onLogin}>
        Accedi
      </Button>
    </div>
  );
};

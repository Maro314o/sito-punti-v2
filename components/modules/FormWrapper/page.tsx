"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ArrowLeftIcon } from "lucide-react";
import { useState } from "react";

export default function FormWrapper() {
  const [page, setPage] = useState<
    "home" | "login" | "register" | "forgot" | "logged"
  >("home");

  return (
    <div className="container mx-auto text-center w-auto md:w-xl lg:w-4xl p-10 md:p-15 lg:p-25">
      {page === "logged" ? (
        <LoggedContent nome={""} cognome={""} classe={""} />
      ) : page === "login" ? (
        <LoginContent
          onBack={() => setPage("home")}
          onRegister={() => setPage("register")}
          onForgotPassword={() => setPage("forgot")}
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
}: {
  onBack: () => void;
  onRegister: () => void;
  onForgotPassword: () => void;
}) => {
  return (
    <div className="grid grid-col gap-5">
      <Button variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>

      <div className="mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
        <Input type="password" placeholder="password" />
      </div>

      <Button variant={"link"} onClick={onForgotPassword}>
        Hai dimenticato la password?
      </Button>

      <div>
        <Button variant={"outline"}>Accedi</Button>
      </div>

      <Button variant={"link"} onClick={onRegister}>
        Non hai un account?
        <br />
        Registrati
      </Button>
    </div>
  );
};

const LoggedContent = ({
  nome,
  cognome,
  classe,
}: {
  nome: string;
  cognome: string;
  classe: string;
}) => {
  return (
    <div className="grid grid-col gap-5">
      <h2>
        {"nome"} {"cognome"}
      </h2>
      <h3>{"classe"}</h3>
    </div>
  );
};

const RegisterContent = ({ onLogin }: { onLogin: () => void }) => {
  return (
    <div className="grid grid-col gap-5">
      <div className="mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
        <Input type="password" placeholder="password" />
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
      <h3>Verrà mandata una mail per il cambio password</h3>
      <Button variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>

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

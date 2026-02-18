"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { ArrowLeftIcon } from "lucide-react";
import { useState } from "react";

export default function FormWrapper({
  p,
}: {
  p?:
    | "home"
    | "login"
    | "register"
    | "forgot"
    | "logged"
    | "profile"
    | "change";
}) {
  const [page, setPage] = useState<
    "home" | "login" | "register" | "forgot" | "logged" | "profile" | "change"
  >(p || "home");
  const nome = "Marco";
  const cognome = "Rossi";
  const classe = "2BE";

  return (
    <div className="container mx-auto text-center grid grid-col gap-5 md:w-xl lg:w-4xl p-10 md:p-15 lg:p-25">
      {page === "logged" ? (
        <LoggedContent nome={nome} cognome={cognome} classe={classe} />
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
      ) : page === "home" ? (
        <HomeContent onLogin={() => setPage("login")} />
      ) : page === "profile" ? (
        <ProfileContent data="10/12/2025" />
      ) : page == "change" ? (
        <ChangeContent />
      ) : null}
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
    <>
      <Button variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>
      <div className="grid grid-col gap-2 mx-auto container max-w-md">
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
    </>
  );
};

const PasswordChangeDialog = () => {
  const [vecchiaPassword, setVecchiaPassword] = useState("");
  const [nuovaPassword, setNuovaPassword] = useState("");
  const [confermaPassword, setConfermaPassword] = useState("");
  const [errore, setErrore] = useState("");
  const [open, setOpen] = useState(false);

  const handleConferma = () => {
    setErrore("");

    if (!vecchiaPassword) {
      setErrore("Inserisci la vecchia password");
      return;
    }

    if (!nuovaPassword) {
      setErrore("Inserisci la nuova password");
      return;
    }

    if (!confermaPassword) {
      setErrore("Conferma la nuova password");
      return;
    }

    if (nuovaPassword !== confermaPassword) {
      setErrore("Password non corrispondenti");
      return;
    }

    // Qui andrebbe la logica per cambiare la password
    console.log("Password cambiata con successo");
    setOpen(false);
    setVecchiaPassword("");
    setNuovaPassword("");
    setConfermaPassword("");
    setErrore("");
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline" size="sm" className="mt-2 w-fit mx-auto">
          Recupera password
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Cambio password</DialogTitle>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="grid gap-2">
            <Input
              type="password"
              placeholder="Vecchia password"
              value={vecchiaPassword}
              onChange={(e) => setVecchiaPassword(e.target.value)}
            />
          </div>
          <div className="grid gap-2">
            <Input
              type="password"
              placeholder="Nuova password"
              value={nuovaPassword}
              onChange={(e) => setNuovaPassword(e.target.value)}
            />
          </div>
          <div className="grid gap-2">
            <Input
              type="password"
              placeholder="Conferma password"
              value={confermaPassword}
              onChange={(e) => setConfermaPassword(e.target.value)}
            />
            {errore && (
              <p className="text-sm text-red-500">{errore}</p>
            )}
          </div>
          <Button onClick={handleConferma}>Conferma</Button>
        </div>
      </DialogContent>
    </Dialog>
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
    <>
      <h2 className="text-3xl">
        {nome} {cognome}
      </h2>
      <h3 className="text-2xl">{classe}</h3>
      <PasswordChangeDialog />
      <p className="text-sm text-muted-foreground">
        Ultimo cambio password: 15/01/2026
      </p>
    </>
  );
};

const RegisterContent = ({ onLogin }: { onLogin: () => void }) => {
  return (
    <>
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
    </>
  );
};

const ForgotContent = ({ onBack }: { onBack: () => void }) => {
  return (
    <>
      <Button variant={"link"} size={"icon"} onClick={onBack}>
        <ArrowLeftIcon />
      </Button>
      <h3>Verrà mandata una mail per il recupero password</h3>
      <div className="mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
      </div>
      <div>
        <Button variant={"outline"}>Invia</Button>
      </div>
    </>
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

const ProfileContent = ({ data }: { data?: string }) => {
  return (
    <>
      <div className="mx-auto w-auto md:w-md">
        <Input type="text" placeholder="mail" />
      </div>
      <div>
        <Button variant={"outline"}>Cambio password</Button>
      </div>
      {data ? <h3>ultimo cambio avvenuto il {data}</h3> : null}
    </>
  );
};

const ChangeContent = () => {
  return (
    <>
      <div className="grid grid-col gap-2 mx-auto w-auto md:w-md">
        <Input type="password" placeholder="vecchia password" />
        <Input type="password" placeholder="password" />
        <Input type="password" placeholder="conferma password" />
      </div>
      <div>
        <Button variant={"outline"}>Conferma</Button>
      </div>
    </>
  );
};

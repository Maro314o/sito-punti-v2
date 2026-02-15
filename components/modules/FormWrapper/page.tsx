"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ArrowLeftIcon } from "lucide-react";
import { useState } from "react";

export default function FormWrapper() {
  const [isLogin, setIsLogin] = useState(false);
  const [isLogged, setIsLogged] = useState(false);
  const [isForgotPw, setIsForgotPw] = useState(false);
  const [isRegister, setIsRegister] = useState(false);
  const LoginPage = () => {
    setIsLogin(true);
  };
  const LoggedPage = () => {
    setIsLogged(true);
  };
  const ForgotPwPage = () => {
    setIsForgotPw(true);
  };
  const RegisterPage = () => {
    setIsRegister(true);
  };
  return (
    <div className="container mx-auto text-center w-auto md:w-xl lg:w-4xl p-10 md:p-15 lg:p-25">
      {isLogin ? (
        <div className="grid grid-col gap-5">
          <Button variant={"link"} size={"icon"}>
            <ArrowLeftIcon />
          </Button>
          <div className="mx-auto w-auto md:w-md">
            <Input type="text" placeholder="mail" />
            <Input type="password" placeholder="password" />
          </div>
          <Button variant={"link"} onClick={ForgotPwPage}>
            Hai dimenticato la password?
          </Button>
          <div>
            <Button variant={"outline"}>Accedi</Button>
          </div>
          <Button variant={"link"} onClick={RegisterPage}>
            Non hai un account?
            <br />
            Registrati
          </Button>
        </div>
      ) : (
        <Button variant={"outline"} onClick={LoginPage}>
          Accedi
        </Button>
      )}
    </div>
  );
}

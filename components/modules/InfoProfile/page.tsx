"use client";

import Image from "next/image";
import Bounty from "../Bounty/page";
import jollyroger from "@/public/class_images/4CI-JOLLY ROGER/THE DIDDLERS.jpg";
import { cn } from "@/lib/utils";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

export default function InfoProfile() {
  const fruttiPos = 3;
  const fruttiNeg = 1;
  const anno = "2026";
  const rotta = "rotta 1";
  const nomeRotta = "Nautilus";
  const ruolo = "Capitano";
  const abilità = "Ambizione del re conquistatore";
  return (
    <div>
      <GeneralitiesWrapper anno={anno} rotta={rotta} nomeRotta={nomeRotta} />
      <div className="container mx-auto grid md:grid-cols-2 md:gap-20 md:p-20 lg:p-30">
        <div className="mx-auto md:order-last flex flex-col justify-center h-full">
          <div className="grid gap-20">
            <Specs ruolo={ruolo} abilità={abilità} />
            <GeneralAbilitiesWrapper />
          </div>
        </div>
        <div className="mx-auto">
          <Friuts fruttiPositivi={fruttiPos} fruttiNegativi={fruttiNeg} />
          <Bounty />
          <div className="container max-w-xs">
            <Image src={jollyroger} alt={""} />
          </div>
        </div>
      </div>
    </div>
  );
}

const GeneralitiesWrapper = ({
  anno,
  rotta,
  nomeRotta,
}: {
  anno: string;
  rotta: string;
  nomeRotta: string;
}) => {
  return (
    <div className="flex flex-row mx-auto justify-evenly mb-10 container p-2 border bg-background shadow-xs whitespace-nowrap rounded-md max-w-xl">
      <div>{anno}</div>
      <div>{rotta}</div>
      <div>{nomeRotta}</div>
    </div>
  );
};

const Friuts = ({
  fruttiPositivi,
  fruttiNegativi,
}: {
  fruttiPositivi: number;
  fruttiNegativi: number;
}) => {
  return (
    <div className="flex flex-col w-48 mx-auto my-5 border-2 border-dashed border-amber-700 bg-amber-50/80 p-3">
      <div className="text-center text-amber-900 text-xs uppercase tracking-widest border-b border-amber-700 pb-1 mb-2">
        Frutti del Mare
      </div>
      <div className="flex flex-row gap-2">
        <div className="flex-1 flex flex-col items-center gap-1">
          <span className="text-2xl">🍎</span>
          <div className="w-full text-center bg-green-700 text-white font-bold text-lg py-1 border-t-4 border-green-900">
            +{fruttiPositivi}
          </div>
        </div>
        <div className="flex-1 flex flex-col items-center gap-1">
          <span className="text-2xl">💀</span>
          <div className="w-full text-center bg-red-800 text-white font-bold text-lg py-1 border-t-4 border-red-950">
            -{fruttiNegativi}
          </div>
        </div>
      </div>
    </div>
  );
};

const Specs = ({
  ruolo,
  abilità,
  isUsed,
}: {
  ruolo: string;
  abilità: string;
  isUsed?: boolean;
}) => {
  return (
    <div className="text-center grid gap-5">
      <div className="border bg-background shadow-xs p-5">
        <h3 className="text-5xl text-bold">{ruolo}</h3>
      </div>
      <div
        className={cn(
          "p-2 border bg-background shadow-xs text-xl",
          isUsed ? "bg-gray-200/50 text-gray-400" : "",
        )}
      >
        <p className="text-3xl">{abilità}</p>
      </div>
    </div>
  );
};

const armiData = {
  poseidon: {
    nome: "POSEIDON",
    descrizione:
      "Permette a chi la utilizza di scegliere eliminare una domanda durante l'interrogazione e sceglierne un'altra al suo posto, tra un elenco di domande disponibili.\n\nPotere presente per ogni pirata.\n\nUtilizzabile una volta in ogni periodo. Nel caso in cui venga scoperto il mistero da parte del pirata o di un membro della sua ciurma, il pirata può decidere di renderlo di nuovo disponibile.",
  },
  pluto: {
    nome: "PLUTON",
    descrizione:
      "Permette a chi la utilizza di raddoppiare i punti di taglia ottenuti con un voto (Verifica, Interrogazione, Progetto). Per essere utilizzata va dichiarato il suo utilizzo prima della prova scelta.\n\nPotere presente per ogni pirata.\n\nUtilizzabile una volta in ogni periodo. Nel caso in cui venga scoperto il mistero da parte del pirata o di un membro della sua ciurma, il pirata può decidere di renderlo di nuovo disponibile.",
  },
  uranus: {
    nome: "URANUS",
    descrizione:
      "Permette a chi la utilizza di rinviare l'interrogazione alla prossima data in cui ci saranno interrogazioni. Per essere utilizzata va dichiarato il suo utilizzo in un'ora di interrogazione, prima di sapere i nomi dei pirati interrogati.\n\nPotere presente per ogni pirata.\n\nUtilizzabile una volta in ogni periodo. Nel caso in cui venga scoperto il mistero da parte del pirata o di un membro della sua ciurma, il pirata può decidere di renderlo di nuovo disponibile.",
  },
};

type ArmaKey = keyof typeof armiData;

const GeneralAbilitiesWrapper = ({}) => {
  const armiUsate: ArmaKey[] = [];

  return (
    <div className="flex flex-row gap-5 mx-auto">
      <GeneralAbility name="poseidon" isUsed={armiUsate.includes("poseidon")} />
      <GeneralAbility name="pluto" isUsed={armiUsate.includes("pluto")} />
      <GeneralAbility name="uranus" isUsed={armiUsate.includes("uranus")} />
    </div>
  );
};

const GeneralAbility = ({
  name,
  isUsed,
}: {
  name: ArmaKey;
  isUsed: boolean;
}) => {
  const arma = armiData[name];

  return (
    <Dialog>
      <DialogTrigger asChild>
        <div className="min-w-25 text-center cursor-pointer hover:opacity-80 transition-opacity">
          <div className="w-30 mx-auto border-2 overflow-hidden border-gray-600 shadow-xs bg-background rounded-full">
            <Image src={jollyroger} alt={name} className="object-cover w-full h-full" />
          </div>
          <h4 className="capitalize">{name}</h4>
        </div>
      </DialogTrigger>
      <DialogContent className="sm:max-w-xl">
        <DialogHeader>
          <DialogTitle>{arma.nome}</DialogTitle>
        </DialogHeader>
        <div
          className={cn(
            "grid gap-4 p-4 rounded-lg border",
            isUsed ? "bg-gray-200/50" : "bg-background"
          )}
        >
          <div className="flex flex-col md:flex-row gap-4 items-start">
            <div className="w-24 h-24 flex-shrink-0 mx-auto md:mx-0">
              <Image
                src={jollyroger}
                alt={arma.nome}
                className="w-full h-full object-cover rounded-full border"
              />
            </div>
            <div className="flex-1">
              <p className="text-sm whitespace-pre-line">{arma.descrizione}</p>
            </div>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
};

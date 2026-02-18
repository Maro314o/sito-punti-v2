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
        <div className="mx-auto md:order-last">
          <div className="grid gap-2">
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
    <div>
      {/* <Image src={""} alt={""} /> !!AGGIUNGERE IMMAGINE FRUTTA*/}
      <table className="text-center">
        <tbody>
          <tr>
            <td className="p-2 border shadow-xs bg-green-400/50 min-w-10">
              +{fruttiPositivi}
            </td>
            <td className="p-2 border shadow-xs bg-red-400/50 min-w-10">
              -{fruttiNegativi}
            </td>
          </tr>
        </tbody>
      </table>
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
    <div className="text-center grid gap-2">
      <div className="p-2 border bg-background shadow-xs rounded-md">
        <h3 className="text-2xl">{ruolo}</h3>
      </div>
      <div
        className={cn(
          "p-2 border bg-background shadow-xs rounded-md text-xl",
          isUsed ? "bg-gray-200/50 text-gray-400" : "",
        )}
      >
        <p>{abilità}</p>
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
    <div className="flex flex-row gap-2 mx-auto">
      <GeneralAbility nome="poseidon" usata={armiUsate.includes("poseidon")} />
      <GeneralAbility nome="pluto" usata={armiUsate.includes("pluto")} />
      <GeneralAbility nome="uranus" usata={armiUsate.includes("uranus")} />
    </div>
  );
};

const GeneralAbility = ({
  nome,
  usata,
}: {
  nome: ArmaKey;
  usata: boolean;
}) => {
  const arma = armiData[nome];

  return (
    <Dialog>
      <DialogTrigger asChild>
        <div className="min-w-25 text-center cursor-pointer hover:opacity-80 transition-opacity">
          <div className="w-10 mx-auto border shadow-xs bg-background rounded-full">
            <Image src={jollyroger} alt={nome} />
          </div>
          <h4 className="capitalize">{nome}</h4>
        </div>
      </DialogTrigger>
      <DialogContent className="sm:max-w-xl">
        <DialogHeader>
          <DialogTitle>{arma.nome}</DialogTitle>
        </DialogHeader>
        <div
          className={cn(
            "grid gap-4 p-4 rounded-lg border",
            usata ? "bg-gray-200/50" : "bg-background"
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

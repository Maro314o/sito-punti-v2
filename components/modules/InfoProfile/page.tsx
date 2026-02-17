import Image from "next/image";
import Bounty from "../Bounty/page";
import jollyroger from "@/public/class_images/4CI-JOLLY ROGER/THE DIDDLERS.jpg";
import { cn } from "@/lib/utils";

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

const GeneralAbilitiesWrapper = ({}) => {
  return (
    <div className="flex flex-row gap-2 mx-auto">
      <GeneralAbility nome={"poseidon"} />
      <GeneralAbility nome={"pluto"} />
      <GeneralAbility nome={"uranus"} />
    </div>
  );
};

const GeneralAbility = ({ nome }: { nome: string }) => {
  return (
    <div className="min-w-25 text-center">
      <div className="w-10 mx-auto border shadow-xs bg-background rounded-full">
        <Image src={jollyroger} alt={""} />
      </div>
      <h4>{nome}</h4>
    </div>
  );
};

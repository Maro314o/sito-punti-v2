import Image from "next/image";
import frame from "@/public/class_images/Taglia.png";
import img from "@/public/class_images/4CI-TAGLIE/GENTILINI.jpeg";
export default function Bounty() {
  return (
    <div className="grid grid-rows-1 container max-w-xs">
      <Image src={img} alt={""} className="col-start-1 row-start-1" />
      <Image src={frame} alt={""} className="col-start-1 row-start-1" />
    </div>
  );
}

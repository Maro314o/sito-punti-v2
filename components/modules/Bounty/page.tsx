import CldImage from "@/components/ui/CldImage";

export default function Bounty() {
  const taglia_img = "SORIA_y8l1gq";
  return (
    <div className="grid grid-rows-1 container max-w-xs">
      <CldImage
        src={taglia_img}
        alt={""}
        width={500}
        height={500}
        className="col-start-1 row-start-1"
      />
      <CldImage
        src="Taglia_wzraop"
        alt={""}
        width={500}
        height={500}
        className="col-start-1 row-start-1"
      />
    </div>
  );
}

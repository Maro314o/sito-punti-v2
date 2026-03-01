import { Button } from "@/components/ui/button";
import CldImage from "@/components/ui/CldImage";

export default function ButtonsWrapper() {
  return (
    <div className="flex flex-row gap-5 mx-auto w-min">
      <div>
        <Button variant={"link"} size={"icon"}>
          <CldImage src="location_gjcgcs" alt={""} width={40} height={40} />
        </Button>
      </div>
      <div>
        <Button variant={"link"} size={"icon"}>
          <CldImage src="mail_v5idey" alt={""} width={40} height={40} />
        </Button>
      </div>
      <div>
        <Button variant={"link"} size={"icon"}>
          <CldImage src="github_jsqzbj" alt={""} width={40} height={40} />
        </Button>
      </div>
    </div>
  );
}

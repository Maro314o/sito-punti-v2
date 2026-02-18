import TitleWrapper from "@/components/modules/TitleWrapper/page";

export default function RottePage() {
  const classe = "2BE";
  
  const rotteData = [
    {
      anno: "1° Anno",
      nomeAnno: "Anno Scolastico 2025-2026",
      rotte: [
        {
          nomeRotta: "Nautilus",
          isole: [
            { nome: "Isola del Saper", argomento: "Matematica - Algebra" },
            { nome: "Isola della Conoscenza", argomento: "Storia - Romani" },
            { nome: "Isola del Sapere", argomento: "Italiano - Grammatica" },
          ]
        }
      ]
    },
    {
      anno: "2° Anno", 
      nomeAnno: "Anno Scolastico 2026-2027",
      rotte: [
        {
          nomeRotta: "Maelstrom",
          isole: [
            { nome: "Isola Geometrica", argomento: "Geometria Euclidea" },
            { nome: "Isola Letteraria", argomento: "Letteratura Italiana" },
          ]
        }
      ]
    },
    {
      anno: "3° Anno",
      nomeAnno: "Anno Scolastico 2027-2028", 
      rotte: [
        {
          nomeRotta: "Oceano Pacifico",
          isole: [
            { nome: "Isola del Calcolo", argomento: "Analisi Matematica" },
            { nome: "Isola Fisica", argomento: "Fisica Moderna" },
            { nome: "Isola Chimica", argomento: "Chimica Organica" },
          ]
        }
      ]
    },
    {
      anno: "4° Anno",
      nomeAnno: "Anno Scolastico 2028-2029",
      rotte: [
        {
          nomeRotta: "Abisso Atlantico",
          isole: [
            { nome: "Isola Tecnologia", argomento: "Informatica Avanzata" },
            { nome: "Isola Economia", argomento: "Economia Aziendale" },
          ]
        }
      ]
    },
    {
      anno: "5° Anno",
      nomeAnno: "Anno Scolastico 2029-2030",
      rotte: [
        {
          nomeRotta: "Alla Fine del Mondo",
          isole: [
            { nome: "Isola Tesi", argomento: "Preparazione Esame" },
            { nome: "Isola Diploma", argomento: "Esame di Stato" },
          ]
        }
      ]
    }
  ];

  return (
    <div className="pt-30">
      <TitleWrapper title="Rotte" />
      
      <div className="container mx-auto p-10 md:p-15 lg:p-25">
        <div className="text-center mb-10">
          <h2 className="text-2xl font-semibold">Classe: {classe}</h2>
        </div>
        
        <div className="max-w-4xl mx-auto space-y-8">
          {rotteData.map((annoData, index) => (
            <div key={index} className="border rounded-lg p-6 bg-background shadow-xs">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                <div>
                  <span className="inline-block bg-primary/10 text-primary px-3 py-1 rounded-full text-sm font-medium mb-2">
                    {annoData.anno}
                  </span>
                  <h3 className="text-xl font-semibold">{annoData.nomeAnno}</h3>
                </div>
              </div>
              
              {annoData.rotte.map((rotta, rottaIndex) => (
                <div key={rottaIndex} className="mt-4 pl-4 border-l-2 border-primary/30">
                  <h4 className="text-lg font-medium text-primary mb-3">
                    1° Rotta: {rotta.nomeRotta}
                  </h4>
                  
                  <div className="space-y-2">
                    {rotta.isole.map((isola, isolaIndex) => (
                      <div 
                        key={isolaIndex} 
                        className="flex flex-col sm:flex-row sm:items-center gap-2 py-2 px-4 bg-muted/50 rounded-md"
                      >
                        <span className="font-medium text-foreground">{isola.nome}</span>
                        <span className="hidden sm:block text-muted-foreground">→</span>
                        <span className="text-muted-foreground">{isola.argomento}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

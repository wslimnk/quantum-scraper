# quantum_scraper/main.py (updated with 170+ deep queries)

from scraper_utils import run_all_scrapers

def smart_queries():
    return [
        # France
        "quantum site:cnrs.fr",
        "quantum site:sorbonne-universite.fr",
        "quantum site:polytechnique.edu",
        "quantum site:ens.fr",
        "quantum site:universite-paris-saclay.fr",
        "quantum startup site:bpifrance.fr",
        "quantum site:incuballiance.fr",
        "quantum site:quantonation.com",

        # Germany
        "quantum site:mpq.mpg.de",
        "quantum site:uni-ulm.de",
        "quantum site:uni-mainz.de",
        "quantum site:fraunhofer.de",
        "quantum startup site:dlr.de",
        "quantum site:htgf.de",
        "quantum site:quantentechnologien.de",
        "quantum site:quantagonia.com",
        "quantum site:munich-quantum-valley.de",

        # Switzerland
        "quantum site:epfl.ch",
        "quantum site:ethz.ch",
        "quantum site:psi.ch",
        "quantum site:venturelab.swiss",
        "quantum site:quantumcenter.ch",

        # Netherlands
        "quantum site:qutech.nl",
        "quantum site:quantuminspire.com",
        "quantum site:tudelft.nl",
        "quantum site:ams-institute.org",
        "quantum startup site:quantumdelta.nl",

        # Nordics
        "quantum site:chalmers.se",
        "quantum site:kth.se",
        "quantum site:aalto.fi",
        "quantum site:sciencenode.org",
        "quantum site:quantumdelta.se",

        # UK
        "quantum site:cam.ac.uk",
        "quantum site:imperial.ac.uk",
        "quantum site:ox.ac.uk",
        "quantum site:ucl.ac.uk",
        "quantum site:bristol.ac.uk",
        "quantum site:techcelerate.ox.ac.uk",
        "quantum startup site:deeptechlabs.tech",
        "quantum site:ukri.org",

        # Southern Europe
        "quantum site:csic.es",
        "quantum site:icfo.eu",
        "quantum site:infn.it",
        "quantum site:catalonia.com",
        "quantum startup site:fi-group.com",
        "quantum site:ptspace.pt",
        "quantum site:institutoptico.pt",

        # EU programs
        "quantum startup site:horizon-europe.ec.europa.eu",
        "quantum startup site:eit.europa.eu",
        "quantum startup site:efsel.eu",
        "quantum startup site:eic.ec.europa.eu",
        "quantum startup site:eu-quantum.eu",

        # University triggers
        "quantum spin-off from university",
        "quantum research group startup",
        "quantum doctoral student startup",
        "quantum project PhD founder",
        "university quantum startup",
        "quantum startup academic founders",
        "professor-founded quantum company",
        "student-built quantum startup",

        # Prizes & grants
        "quantum startup awarded grant",
        "quantum startup wins competition",
        "quantum startup innovation award",
        "quantum company grant recipient",
        "quantum prize winner startup",
        "quantum startup Bpifrance",
        "quantum startup grant NSF",

        # Incubators
        "quantum startup joined accelerator",
        "quantum incubator announcement",
        "quantum accelerator cohort",
        "quantum startup hello tomorrow",
        "quantum company deeptech labs",
        "quantum site:startupbootcamp.org",
        "quantum site:hellotomorrow.org",
        "quantum site:entrepreneurfirst.org",

        # Stealth & hiring
        "quantum startup stealth mode",
        "quantum startup hiring CTO",
        "quantum startup job opening",
        "quantum startup new office",

        # Bonus catch-alls
        "quantum AND (accelerator OR incubator OR phd OR spin-off OR commercialization OR grant OR award OR prize)",
        "quantum site:* university technology transfer office",
        "quantum site:* spin-off office",
    ]

if __name__ == "__main__":
    run_all_scrapers(queries=smart_queries())


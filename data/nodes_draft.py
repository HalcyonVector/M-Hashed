# Real coordinates sourced from OpenStreetMap (queried live via Overpass API).
# id, name, type, lat, lon, source_note
NODES_RAW = [
    ("MAIN","NH66 / Karkala Road Junction (east of Manipal)","main",13.3430,74.8010,"osm_road"),

    ("SS1","Manipal Substation","substation",13.3318,74.7882,"osm"),
    ("SS2","Doddanagudde Substation","substation",13.3657,74.7437,"osm"),
    ("SS3","Muluru Substation","substation",13.2084,74.7649,"osm"),

    ("WP1","Malpe Water Pumping Station","pump",13.3490,74.7080,"estimated"),
    ("WP2","Kaup Water Works","pump",13.2280,74.7440,"estimated"),
    ("WP3","Manipal Reservoir Pumping Station","pump",13.3480,74.7920,"estimated"),

    ("H1","District Hospital, Udupi","hospital",13.3340,74.7423,"osm"),
    ("H2","TMA Pai Hospital","hospital",13.3326,74.7472,"osm"),
    ("H3","KMC Hospital, Manipal","hospital",13.3535,74.7894,"osm"),

    ("S1","Government High School, Udupi","school",13.3311,74.7424,"osm"),
    ("S2","Manipal Pre-University College","school",13.3465,74.7871,"osm"),
    ("S3","Adiudupi Higher Primary School","school",13.3481,74.7327,"osm"),

    ("SH1","Doddanagudde Government School","shelter",13.3580,74.7556,"osm"),
    ("SH2","St Cecily's Girls High School","shelter",13.3360,74.7428,"osm"),

    ("R1","Malpe","residential",13.3507,74.7037,"osm"),
    ("R2","Kodavoor","residential",13.3530,74.7101,"osm"),
    ("R3","Kapu (Kaup)","residential",13.2307,74.7484,"osm"),
    ("R4","Katapady","residential",13.2824,74.7462,"osm"),
    ("R5","Manipal","residential",13.3520,74.7870,"osm"),
    ("R6","Indrali","residential",13.3453,74.7713,"osm"),
    ("R7","Brahmagiri","residential",13.3412,74.7408,"osm"),

    ("B1","Malpe Bridge","bridge",13.3400,74.7074,"osm"),
    ("B2","Unnamed creek crossing near Kaup","bridge",13.2629,74.7325,"osm"),
    ("B3","Malpe-Manipal Road Bridge","bridge",13.3455,74.7705,"osm"),

    ("RD1","NH66 junction, Udupi","road",13.3430,74.7460,"osm_road"),
    ("RD2","NH66 junction, Katapady","road",13.2820,74.7460,"osm_road"),
    ("RD3","Malpe-Manipal Road junction","road",13.3450,74.7800,"osm_road"),
    ("RD4","Udupi-Manipal link junction","road",13.3360,74.7600,"osm_road"),
    ("RD5","Manipal approach junction","road",13.3500,74.7830,"osm_road"),
]

if __name__ == "__main__":
    print(",".join(f"{lat},{lon}" for (_,_,_,lat,lon,_) in NODES_RAW))

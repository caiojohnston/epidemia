CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

CREATE TABLE IF NOT EXISTS municipios (
    id SERIAL PRIMARY KEY,
    codigo_ibge VARCHAR(7) UNIQUE NOT NULL,
    nome VARCHAR(255) NOT NULL,
    uf CHAR(2) NOT NULL,
    geom GEOMETRY(MULTIPOLYGON, 4326),
    populacao INTEGER,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_municipios_geom ON municipios USING GIST(geom);
CREATE INDEX IF NOT EXISTS idx_municipios_uf ON municipios(uf);
CREATE INDEX IF NOT EXISTS idx_municipios_codigo_ibge ON municipios(codigo_ibge);

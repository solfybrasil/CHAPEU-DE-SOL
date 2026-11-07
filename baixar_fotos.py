"""
Baixa TODAS as fotos do site atual do Camping Chapéu de Sol, organizadas por pasta.

Uso:  python baixar_fotos.py        (só precisa de Python 3, nada para instalar)

Resultado:
  fotos/
    hospedagens/
      chale-madeira/   capa + fotos do chalé
      chale-vip/
      pousada/
      suite-container/
      trailer/
      barraca/         área de camping (banheiros, cozinhas, barracas)
      ready-camp/
      glamping/
      day-use/
    tabelas-de-preco/  artes de preço de cada hospedagem (por temporada)
    galeria/           fotos gerais de lazer (as sem pista no nome viram "a-identificar-XX")
    _lista.csv         arquivo, pasta, url_original
Fotos repetidas entre páginas são baixadas uma vez só e copiadas.
"""
import os, csv, time, shutil, urllib.request

U = "https://campingchapeudesol.com.br/wp-content/uploads/"

# ------------------------------------------------------------------ HOSPEDAGENS
# (pasta, nome do arquivo, [urls candidatas — tenta a 1ª, se falhar a próxima])
H = []
def add(pasta, nome, *caminhos):
    H.append((pasta, nome, [U + c for c in caminhos]))

# Chalé Madeira
add("hospedagens/chale-madeira", "capa", "2026/01/be3db78d-15ea-4768-ac25-e1967ca2dd95-2048x1790.jpg", "2026/01/be3db78d-15ea-4768-ac25-e1967ca2dd95-1024x895.jpg")
add("hospedagens/chale-madeira", "capa-2", "2025/11/chale.jpeg")
for i, c in enumerate(["2025/07/IMG_3411.jpg", "2025/07/IMG_3405.jpg", "2025/07/IMG_3400.jpg", "2025/07/IMG_3399.jpg",
                       "2024/04/IMG_4857.jpg", "2024/04/8FEA3C13-3154-462B-92D8-E3898D20212E_L0_001-27_11_2022-11_12_49-am.jpg",
                       "2024/04/IMG_0256.jpg", "2024/04/IMG_4845.jpg", "2024/04/IMG_6555.jpg", "2024/04/IMG_6571.jpg"], 1):
    add("hospedagens/chale-madeira", f"chale-madeira-{i:02d}", c)

# Chalé VIP
add("hospedagens/chale-vip", "capa", "2025/08/CHALE-VIP.jpg")
add("hospedagens/chale-vip", "capa-2", "2025/05/chale-vip-2022-02-01.jpg", "2025/05/chale-vip-2022-02-01-1024x768.jpg")
for i, c in enumerate(["2025/08/CHALE-VIP-2.jpg", "2025/08/CHALE-VIP-3.jpg", "2025/08/IMG_3420-scaled.jpg", "2025/08/IMG_3423-scaled.jpg",
                       "2025/08/IMG_3424-scaled.jpg", "2025/08/IMG_3426-scaled.jpg", "2025/08/IMG_3428-scaled.jpg",
                       "2025/08/IMG_3429-scaled.jpg", "2025/08/IMG_3430-scaled.jpg", "2025/08/IMG_3441-scaled.jpg"], 1):
    add("hospedagens/chale-vip", f"chale-vip-{i:02d}", c)

# Pousada
add("hospedagens/pousada", "capa", "2026/01/pousadaJPG-scaled.jpg", "2026/01/pousadaJPG-768x1024.jpg")
add("hospedagens/pousada", "fachada", "2026/01/Pousada-Fachada.jpg")
add("hospedagens/pousada", "pousada-interior", "2025/08/Pousada-interior.jpg")
for i in range(2, 6):
    add("hospedagens/pousada", f"pousada-{i-1:02d}", f"2025/08/POUSADA-{i}.jpg")

# Suíte Container
add("hospedagens/suite-container", "capa", "2025/08/suite-container-02-2048x1145.jpeg", "2025/08/suite-container-02-scaled.jpeg")
for i in range(1, 6):
    add("hospedagens/suite-container", f"suite-container-{i:02d}", f"2025/08/suite-container-0{i}-scaled.jpeg")

# Trailer
add("hospedagens/trailer", "capa", "2026/01/capatrailerJPG-2048x1536.jpg", "2026/01/capatrailerJPG-1024x768.jpg")
for nome, c in [("trailer-exterior", "2025/08/Trailer-exterior.jpg"), ("trailer-exterior-2", "2025/08/Trailer-exterior-2.jpg"),
                ("trailer-interior", "2025/08/Trailer-interior.jpg"), ("trailer-interior-2", "2025/08/Trailer-interior-2.jpg"),
                ("trailer-beliche", "2025/08/Trailer-Beliche.jpg"), ("trailer-banheiro", "2025/08/Trailer-banheiro.jpg"),
                ("trailer-01", "2025/08/Trailer-1.jpg"), ("trailer-02", "2025/08/Trailer.jpg"),
                ("trailer-03", "2024/04/b31fc6f5-ffc1-40fe-9042-9d5ea7be5227.jpg"), ("trailer-04", "2024/04/a92cf6a6-5f66-4ee2-b5bd-d870390064ce.jpg")]:
    add("hospedagens/trailer", nome, c)

# Barraca (área de camping)
add("hospedagens/barraca", "capa", "2026/03/PHOTO-2026-02-21-18-41-11.jpg", "2026/03/PHOTO-2026-02-21-18-41-11-768x1024.jpg")
for nome, c in [("banheiro-camping", "2025/08/Imagem-Banheiro-Camping.jpg"), ("cozinha-comunitaria", "2025/08/COZINHA.jpg"),
                ("cozinha-comunitaria-2", "2025/08/COZINHA-2.jpg"), ("cozinha-comunitaria-3", "2025/08/COZINHA-3.jpg"),
                ("cozinha-comunitaria-4", "2024/04/Cozinha-1-scaled.jpg"),
                ("camping-geral", "2025/08/CAMPING.jpg"), ("camping-foto", "2025/08/Camping-foto.jpg"),
                ("camping-barracas", "2025/08/Camping-barracas.jpg"), ("camping-area-do-galpao", "2025/08/Camping-area-do-galpao.jpg"),
                ("camping-01", "2025/08/Camping-1.jpg"), ("camping-02", "2025/08/CAMPING-2.jpg"), ("camping-03", "2025/08/CAMPING-3.jpg"),
                ("camping-04", "2025/08/CAMPING-4.jpg"), ("camping-05", "2025/08/CAMPING-5.jpg"), ("camping-07", "2025/08/CAMPING-7.jpg"),
                ("camping-08", "2025/08/CAMPING-8.jpg"), ("camping-09", "2025/08/CAMPING-9.jpg"), ("camping-10", "2025/08/CAMPING-10.jpg"),
                ("camping-gopro", "2025/07/CAMPING-4.jpg"), ("camping-2022", "2022/10/camping-chapeu-de-sol-2022.jpg"),
                ("camping-2022-v02", "2022/10/camping-chapeu-de-sol-2022-v02.jpg"), ("camping-22-02-17", "2022/02/camping-22-02-17.jpg"),
                ("area-de-barracas-eucaliptos", "2021/08/area-de-barracas-eucaliptos-chapeu-de-sol-unicode-encoding-conflict.jpg")]:
    add("hospedagens/barraca", nome, c)

# Ready Camp
add("hospedagens/ready-camp", "capa", "2026/06/Imagem-barraca-site.png", "2026/06/Imagem-barraca-site-1024x1024.png")
add("hospedagens/ready-camp", "ready-camp", "2026/06/Ready-Camp.jpeg")
for i, c in enumerate(["2026/06/WhatsApp-Image-2026-06-09-at-2.41.56-PM.jpeg", "2026/06/WhatsApp-Image-2026-06-09-at-2.41.56-PM-1.jpeg",
                       "2026/06/WhatsApp-Image-2026-06-09-at-2.41.57-PM.jpeg", "2026/06/WhatsApp-Image-2026-06-09-at-2.46.58-PM.jpeg",
                       "2026/06/WhatsApp-Image-2026-06-09-at-2.46.59-PM-scaled.jpeg"], 1):
    add("hospedagens/ready-camp", f"ready-camp-{i:02d}", c)
add("hospedagens/ready-camp", "banheiros", "2026/06/Imagem-banheiros.jpeg")

# Glamping
add("hospedagens/glamping", "capa", "2026/06/Glamping-1.png", "2026/06/Glamping-1-1024x1024.png")

# Day Use
add("hospedagens/day-use", "capa", "2022/02/lazer-2022-02-19.jpg")
add("hospedagens/day-use", "quadra-de-tenis", "2025/08/QUADRA-DE-TENIS.jpg")

# ------------------------------------------------------------- TABELAS DE PREÇO
def tab(slug, *arquivos):
    for i, a in enumerate(arquivos, 1):
        base, ext = os.path.splitext(a)
        cands = [a] if not base.endswith("-819x1024") else [base[:-9] + ext, a]
        add(f"tabelas-de-preco/{slug}", f"{slug}-{i:02d}-{os.path.basename(base).replace('-819x1024','').lower()}", *cands)

tab("chale-madeira", "2026/10/OutubroDezembroMadeira-819x1024.jpg", "2026/10/OUTUBROFDSMADEIRA-819x1024.jpg", "2026/09/17-3-819x1024.jpg",
    "2026/10/Madeiranatal2-819x1024.jpg", "2026/10/MADEIRA2027-819x1024.jpg")
tab("chale-vip", "2026/10/vipsemana-819x1024.jpg", "2026/10/vipfds-819x1024.jpg", "2026/09/18-3-819x1024.jpg", "2026/10/VIPNATAL-819x1024.jpg")
tab("pousada", "2026/10/POUSADASEMANA2-819x1024.jpg", "2026/10/POUSADAFDS2-819x1024.jpg", "2026/09/19-3-819x1024.jpg",
    "2026/10/POUSADANATAL2-819x1024.jpg", "2026/10/POUSADA2027-819x1024.jpg")
tab("suite-container", "2026/10/containerdiasemana-819x1024.jpg", "2026/10/conntainerfds-819x1024.jpg", "2026/09/20-1-819x1024.jpg",
    "2026/10/containernatal2-819x1024.jpg", "2026/10/containeranonovo2-819x1024.jpg")
tab("trailer", "2026/10/trailersemana-819x1024.jpg", "2026/10/trailerfds-819x1024.jpg", "2026/09/16-2-819x1024.jpg", "2026/10/trailernatal-819x1024.jpg")
tab("barraca", "2026/10/BarracaOutubroDezembro.jpg", "2026/11/VALORESNOVOSSITE-Post-para-Instagram-4_5.jpg", "2026/10/BARRACANATAL.jpg", "2026/10/BARRACA2027.jpg")
tab("ready-camp", "2026/10/REadyCampOutubroDezembro-819x1024.jpg", "2026/11/VALORESNOVOSSITE-Post-para-Instagram-4_5-3-819x1024.jpg",
    "2026/10/ReadyCampNatal-819x1024.jpg", "2026/10/ReadyCamp2027-819x1024.jpg")
tab("day-use", "2026/10/dayusedezembro.jpg")

# ----------------------------------------------------------------------- GALERIA
GAL = [
    ("2026/01/FotoCapaSite-scaled.jpg", "capa-site"), ("2026/01/Piscinafeijao-scaled.jpg", "piscina-feijao-2"),
    ("2026/01/Pisciinfantil25-scaled.jpg", "piscina-infantil-2"), ("2026/06/Pesqueiro.jpeg", "pesqueiro"),
    ("2026/06/Piscina-Feijao-velha.jpeg", "piscina-feijao-antiga"), ("2026/06/Pesqueiro-velha.jpeg", "pesqueiro-antigo"),
    ("2026/06/Imagem-piscina.jpeg", "piscina"), ("2026/06/Quadra-de-tenis.jpeg", "quadra-de-tenis"),
    ("2026/06/FOTO-PISCINA-CENTRAL-scaled.jpg", "piscina-central"), ("2026/06/Imagem-tirolesa.jpeg", "tirolesa"),
    ("2026/06/Piscina-feijao.jpeg", "piscina-feijao"), ("2026/06/Foto-piscina-das-criancas-.jpeg", "piscina-infantil"),
    ("2021/08/area-barracas-quadra-de-tenis-300x225-1.png", "area-de-barracas-quadra-de-tenis"),
]
SEM_NOME = [
    "2022/02/lazer-2022-02-19.jpg", "2026/01/EA81B6C0-9B3D-4046-A58D-4776B49DB14C.jpg", "2026/01/261e27c4-2d2b-4d65-8ffd-ddde549136b8-scaled.jpg",
    "2026/01/5f64e1d9-c12c-4c04-9cf0-ac3b7edcc769.jpg", "2026/01/8dbb8150-ecdb-4031-87d5-13f09b38b28d-scaled.jpg",
    "2025/08/IMG_3447-scaled.jpg", "2025/08/IMG_3450-scaled.jpg", "2025/08/IMG_3451-scaled.jpg", "2025/08/IMG_3458-scaled.jpg",
    "2025/08/IMG_3459-scaled.jpg", "2025/08/IMG_3460-scaled.jpg", "2025/08/IMG_3462-scaled.jpg", "2025/08/IMG_3465-scaled.jpg",
    "2025/08/IMG_3467-scaled.jpg", "2025/08/IMG_3468-scaled.jpg", "2025/08/IMG_3469-scaled.jpg", "2025/08/IMG_3471-scaled.jpg",
    "2025/08/IMG_3472-scaled.jpg", "2025/08/IMG_3475-scaled.jpg", "2025/08/IMG_3482-scaled.jpg", "2025/08/IMG_3484-scaled.jpg",
    "2021/08/ocamping-01.jpg", "2021/08/ocamping-01-1.jpg", "2021/08/ocamping-02.jpg", "2021/08/home-01.jpg", "2021/08/home-02.jpg",
    "2021/08/home-02-1.jpg", "2021/08/home-04.jpg", "2021/08/img-9723-768x512-1.jpg", "2021/08/img-0237.jpg", "2021/08/img-0456.jpg",
    "2021/08/imagem-861.jpg", "2021/08/img-4433-2.jpg", "2021/08/imagem-542.jpg", "2021/08/imagem-467.jpg", "2021/08/img-9943-1.jpg",
    "2021/08/img-6484-650x470-1.jpg", "2021/08/img-6506-650x470-1.jpg", "2021/08/img-6522-667x700-1.jpg", "2021/08/img-6532.jpg",
    "2021/08/img-0442-768x512-1.jpg", "2021/08/img-0443.jpg", "2021/08/img-1078.jpg", "2021/08/img-5574.jpg", "2021/08/img-3411.jpg",
    "2021/08/img-2264.jpg", "2021/08/img-9881.jpg",
] + [f"2022/02/lazer-2022-02-{d:02d}.jpg" for d in range(1, 21) if d not in (10, 19)] + ["2022/02/lazer-2022-02-10.jpg"]
for c, n in GAL:
    add("galeria", n, c)
for i, c in enumerate(SEM_NOME, 1):
    add("galeria", f"a-identificar-{i:02d}", c)

# ------------------------------------------------------------------- DOWNLOAD
baixados = {}            # url -> arquivo local (para não baixar 2x)
linhas, falhas = [], []
def baixar(url, destino):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as r, open(destino, "wb") as f:
        f.write(r.read())

for pasta, nome, cands in H:
    os.makedirs(os.path.join("fotos", pasta), exist_ok=True)
    feito = False
    for url in cands:
        ext = os.path.splitext(url)[1].lower().replace(".jpeg", ".jpg")
        destino = os.path.join("fotos", pasta, nome + ext)
        if os.path.exists(destino):
            feito = True; break
        try:
            if url in baixados:
                shutil.copyfile(baixados[url], destino)
            else:
                baixar(url, destino); baixados[url] = destino; time.sleep(0.25)
            linhas.append([nome + ext, pasta, url]); print("ok  ", destino); feito = True; break
        except Exception as e:
            if os.path.exists(destino): os.remove(destino)
            last = e
    if not feito:
        falhas.append((pasta, nome, cands[0], str(last))); print("ERRO", pasta, nome, last)

with open(os.path.join("fotos", "_lista.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["arquivo", "pasta", "url_original"]); w.writerows(linhas)

print(f"\n{len(linhas)} arquivos salvos em ./fotos  |  {len(falhas)} falhas")
for p, n, u, e in falhas:
    print(f"  - {p}/{n}: {u} ({e})")

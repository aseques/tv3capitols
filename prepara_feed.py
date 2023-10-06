"""
Codi generat per chatgpt per detectar els casos on hi ha temporades i obtenir el valor del 
selector de temporades
"""

from bs4 import BeautifulSoup

html = """
<div class="M-selectorTemporades T-alacartaTema">
    <div class="visible-ui-native wrapper-native">
        <select name="selectorTemporades-mobile" id="selectorTemporades-mobile" onchange="window.location.href=this.value;">
            <option value="https://www.ccma.cat/tv3/au-pair/temporada-3/" selected>Temporada 3</option>
            <option value="https://www.ccma.cat/tv3/au-pair/temporada-2/">Temporada 2</option>
            <option value="https://www.ccma.cat/tv3/au-pair/temporada-1/">Temporada 1</option>
        </select>
    </div>
    <div class="dropdown R-noNative hidden-ui-native">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
            <span class="literal">Temporada 3</span>
            <span class="ico-arrow-down2"></span>
        </a>
        <ul class="dropdown-menu mobileNavDrop" role="menu">
            <li><a class="dropdown-element selected" href="https://www.ccma.cat/tv3/au-pair/temporada-3/" title="Capítols de la temporada 3">Temporada 3</a></li>
            <li><a class="dropdown-element" href="https://www.ccma.cat/tv3/au-pair/temporada-2/" title="Capítols de la temporada 2">Temporada 2</a></li>
            <li><a class a href="https://www.ccma.cat/tv3/au-pair/temporada-1/" title="Capítols de la temporada 1">Temporada 1</a></li>
        </ul>
    </div>
</div>
"""

# Analitzar l'HTML amb BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Trobar el selector de temporades
selector_temporades = soup.find('select', {'id': 'selectorTemporades-mobile'})

# Obtenir les opcions del selector
opcions = selector_temporades.find_all('option')

# Recórrer les opcions i imprimir el valor i el text
for opcio in opcions:
    valor = opcio['value']
    text = opcio.get_text()
    print(f"Valor: {valor}, Text: {text}")

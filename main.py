# Skills Test - 2nd Quarter
from pyscript import display, document
non_metals = {
    "H": ("H", "Hydrogen", "1", "1.008"),
    "He": ("He", "Helium", "2", "4.0026"),
    "C": ("C", "Carbon", "6", "12.011"),
    "N": ("N", "Nitrogen", "7", "14.007"),
    "O": ("O", "Oxygen", "8", "15.999"),
    "F": ("F", "Fluorine", "9", "18.998"),
    "Ne": ("Ne", "Neon", "10", "20.180"),
    "P": ("P", "Phosphorus", "15", "30.974"),
    "S": ("S", "Sulfur", "16", "32.06"),
    "Cl": ("Cl", "Chlorine", "17", "35.45"),
    "Ar": ("Ar", "Argon", "18", "39.948"),
    "Se": ("Se", "Selenium", "34", "78.971"),
    "Br": ("Br", "Bromine", "35", "79.904"),
    "Kr": ("Kr", "Krypton", "36", "83.798"),
    "I": ("I", "Iodine", "53", "126.90"),
    "Xe": ("Xe", "Xenon", "54", "131.29"),
    "Rn": ("Rn", "Radon", "86", "222"),
    "Og": ("Og", "Oganesson", "118", "294")
}


def search_element(e):
    document.getElementById("result").innerHTML = ""

    element1 = document.getElementById("element").value.strip().title()

    element_details = non_metals.get(element1, ("Element not found", "-", "-", "-"))

    document.getElementById("result").innerHTML = f"""

<b>Symbol</b>: {element_details[0]}<br>
<b>Element</b>: {element_details[1]}<br>
<b>Atomic Number</b>: {element_details[2]}<br>
<b>Atomic Mass</b>: {element_details[3]}<br>
"""
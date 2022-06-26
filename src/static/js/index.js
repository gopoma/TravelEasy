document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".messages__closer").forEach(messageCloser => {
        messageCloser.onclick = function() {
            messageCloser.parentNode.parentNode.removeChild(messageCloser.parentNode);
        }
    });

    const switchEnableSearch = document.querySelector("#switchEnableSearch");
    const searchForm = document.querySelector("#searchForm");
    switchEnableSearch?.addEventListener("click", function() {
        if(!switchEnableSearch.checked) {
            searchForm.innerHTML = "";
        } else {
            searchForm.innerHTML = `
                <table border="1">
                    <tr>
                        <td>
                            <b>Nombre Ciudad</b><input type="checkbox" id="nombreCiudadMark" onclick="toggleNombreCiudadInput()">
                        </td>
                        <td id="nombreCiudadInputContainer"></td>
                    </tr>
                    <tr>
                        <td>
                            <b>Oferta Tour</b><input type="checkbox" id="ofertaTourMark" onclick="toggleOfertaTourInput()">
                        </td>
                        <td id="ofertaTourInputContainer"></td>
                    </tr>
                </table>
                <input type="submit" value="Search">
            `;
        }
    });

    searchForm.addEventListener("submit", evt => {
        evt.preventDefault();
        const searchForm = evt.target;
        const { ofertaTour } = searchForm;
        searchForm.style.display = "none";
        if(ofertaTour) {
            ofertaTour.value = ofertaTour.checked ? "on" : "off";
            ofertaTour.checked = true;
        }
        searchForm.submit();
    });
});

function toggleNombreCiudadInput() {
    const nombreCiudadMark = document.querySelector("#nombreCiudadMark");
    const nombreCiudadInputContainer = document.querySelector("#nombreCiudadInputContainer");
    if(!nombreCiudadMark.checked) {
        nombreCiudadInputContainer.innerHTML = "";
    } else {
        nombreCiudadInputContainer.innerHTML = "<input type='text' name='nombreCiudad'>";
    }
}

function toggleOfertaTourInput() {
    const ofertaTourMark = document.querySelector("#ofertaTourMark");
    const ofertaTourInputContainer = document.querySelector("#ofertaTourInputContainer");
    if(!ofertaTourMark.checked) {
        ofertaTourInputContainer.innerHTML = "";
    } else {
        ofertaTourInputContainer.innerHTML = "<input type='checkbox' name='ofertaTour'>"
    }
}
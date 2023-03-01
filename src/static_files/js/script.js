

const savePreset = async (preset) => {
    try {
        await fetch("api/preset", {
            method: "POST",
            body: JSON.stringify(preset)
        });
     } catch(ex) {

     }
}


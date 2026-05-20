function showProfile(){
    const petName = "Biscuit"
    const age = 3
    let breed = "Husky"
    let mood = "Playfull and very active"
    let owner = null
    let vacci = null
    let rescuestory;
    {
        var shelter = "Happy Paws Shelter"
        let shelterCode = "HP-2024"
        console.log(shelterCode)
    }
    let adoptionAge = 3
    let ageMatch = (age == adoptionAge)
    let microchipID = "MC-2024"
    let scannerChipID = "MC-2024"
    let chipMatch = (microchipID == scannerChipID)
    console.log(petName)
    console.log(age)
    console.log(breed)
    console.log(mood)
    console.log(owner)
    console.log(vacci)
    console.log(rescuestory)
    console.log(shelter)
    console.log(ageMatch)
    console.log(chipMatch)
}
showProfile()
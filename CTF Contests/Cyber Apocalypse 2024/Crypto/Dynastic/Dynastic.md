# Dynastic - Very Easy

### Description
> You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!

### 1. 
> Reading the description, I realized that part of it would require the a caesar cipher to decrypt. With the provided files, there seems to be some identity mapping. First, I thought maybe (probably not) we could plug the encrypted flag into a ROT13 function and get the flag. Did not work. 

### 2. 
> Then it came to reversing the identity mapping. Which just involved reversing the steps in the python script. Flag acquired after reversing the identity mapping function. 
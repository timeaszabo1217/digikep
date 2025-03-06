# Digitális képfeldolgozás

Jelen projekt során egy TARDIS modellt valósítottam meg Blenderben, miközben az OpenCV segítségével egy űrt ábrázoló digitális képfeldolgozást készítettem, kombinálva a 3D modellezést és a képi effektusokat a valósághű űrélmény létrehozásához.

## Feladat szöveges leírása
A Digitális képfeldolgozás tantárgy során a félév beadandói OpenCV segítségével kerülnek elkészítésre. Az OpenCV egy széles körben használt képfeldolgozó könyvtár, amely C++ alapú, de Python és Java nyelvi kötésekkel is rendelkezik. A félév célja a képfeldolgozás alapvető és magasabb szintű eljárásainak alkalmazása, valamint az OpenCV használatának gyakorlati elsajátítása. A tantárgy során több gyakorlati feladatot oldunk meg, amelyek segítségével mélyebb ismereteket szerzünk a digitális képek feldolgozásában és elemzésében.

### Követelmények

#### 1. Képfeldolgozó feladatok:
- **Pontműveletek**: Használjunk pontoperációkat, mint inverzió, gamma korrekció, fényesség/kontraszt beállítás, küszöbölés és vágás.
- **Zajcsökkentés és szűrés**: Képzaj hozzáadása és szűrők alkalmazása, konvolúciós operátorok használata a képek tisztítására.
- **Morfológiai műveletek**: Erózió és dilatáció alkalmazása, hogy segítsenek a képek formájának megváltoztatásában.
- **Éldetektálás**: Használjunk éldetektáló algoritmusokat, mint a Sobel és Canny operátorokat.
- **Alakzatelemzés**: A képek geometriai alakzatait (például egyenesek, körök) detektáljuk és jellemzőiket mérjük.

#### 2. Magasabb szintű műveletek:
- **Szegmentálás**: Alkalmazzunk különböző szegmentációs módszereket, mint adaptív küszöbölés, régiónövelés és GrabCut.
- **Kontúrok és alakzatelemzés**: Alakzatelemzési feladatok, mint körök, egyenesek detektálása és azok jellemzőinek kiszámítása.

#### 3. Technikai feladatok:
- **Videófeldolgozás**: Dinamikus képfeldolgozás videófolyamokban.
- **Képmegjelenítés és eseménykezelés**: Az OpenCV és Matplotlib könyvtárak használatával jelenítsük meg a feldolgozott képeket, és alkalmazzunk interaktív eseménykezelést.

### Dokumentáció és kód
A beadandóhoz mellékelt dokumentáció és kód az alábbiakat kell, hogy tartalmazza:
1. **Feladatok részletes leírása**: Minden képfeldolgozó algoritmus alkalmazása előtt egy részletes leírás arról, hogy miért és hogyan választottuk azt a megoldást.
2. **Alkalmazott algoritmusok magyarázata**: A használt OpenCV függvények és módszerek leírása, illetve azok működésének magyarázata.
3. **Programkód**: A teljes programkód, amely tartalmazza a képfeldolgozó műveleteket, mint például a képek beolvasása, feldolgozása, és az eredmények kiírása.
4. **Vizualizált eredmények**: A feldolgozott képek és azok változásainak bemutatása, például előtte-utána képek, hisztogramok és más vizualizációk.
5. **Elemzés és következtetések**: Minden feladathoz mellékelni kell az elemzést, hogy az alkalmazott képfeldolgozási módszerek hogyan befolyásolták az eredményeket, és hogyan lehetne továbbfejleszteni a megoldást.

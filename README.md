# Webcam AI Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange.svg)](https://mediapipe.dev)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](README.md)

> **🎯 Controllo Gestuale di Poligoni con Intelligenza Artificiale**

Un tool AI innovativo che utilizza la webcam per rilevare i gesti della mano e modificare dinamicamente poligoni sullo schermo in tempo reale.

## 📋 Indice

- [Descrizione](#descrizione)
- [Caratteristiche](#caratteristiche)
- [Prerequisiti](#prerequisiti)
- [Installazione](#installazione)
- [Utilizzo](#utilizzo)
- [Controlli Gestuali](#controlli-gestuali)
- [Poligoni Supportati](#poligoni-supportati)
- [Risoluzione Problemi](#risoluzione-problemi)
- [Tecnologie Utilizzate](#tecnologie-utilizzate)

## 📖 Descrizione

Webcam AI Tool è un'applicazione di computer vision che combina il riconoscimento gestuale con la manipolazione grafica in tempo reale. Utilizzando algoritmi di machine learning avanzati, il tool rileva i movimenti delle dita e li traduce in comandi per modificare forme geometriche sullo schermo.

## ✨ Caratteristiche

- **🤖 Riconoscimento AI**: Utilizza MediaPipe per il tracking preciso delle mani
- **🎮 Controllo Intuitivo**: Gesti naturali per controllare i poligoni
- **📊 Visualizzazione Real-time**: Feedback visivo immediato e fluido
- **🎨 Interfaccia Moderna**: UI pulita con informazioni dettagliate
- **⚡ Performance Ottimizzate**: Elaborazione veloce e responsiva
- **🔧 Configurazione Flessibile**: Parametri personalizzabili

## 🔧 Prerequisiti

Prima di iniziare, assicurati di avere:

- **Python 3.8+** installato sul sistema
- **Webcam funzionante** (integrata o USB)
- **Illuminazione adeguata** per il riconoscimento ottimale
- **Connessione internet** per l'installazione delle dipendenze

## 🚀 Installazione

### Passo 1: Clona o scarica il progetto
```bash
git clone [repository-url]
cd webcam-ai-tool
```

### Passo 2: Installa le dipendenze
```bash
pip install -r requirements.txt
```

### Passo 3: Verifica l'installazione
```bash
python tool.py --version
```

## 🎮 Utilizzo

### Avvio Rapido

```bash
# Avvia l'applicazione
python tool.py
```

### Primo Utilizzo

1. **Posizionamento**: Siediti davanti alla webcam con buona illuminazione
2. **Calibrazione**: Mostra la mano aperta davanti alla camera
3. **Controllo**: Usa pollice e indice per controllare il poligono
4. **Uscita**: Premi 'q' per terminare l'applicazione

## 🤏 Controlli Gestuali

| Gesto | Azione | Risultato |
|-------|--------|-----------|
| 🤏 **Allargamento** | Aumenta distanza pollice-indice | ➕ Aggiunge un lato |
| 🤌 **Restringimento** | Diminuisce distanza pollice-indice | ➖ Rimuove un lato |
| ✋ **Mano aperta** | Mostra tutti i landmark | 🔍 Modalità debug |
| ❌ **Nessuna mano** | Nessun rilevamento | ⏸️ Pausa controlli |

### Parametri di Controllo

- **Range lati**: 3-20 lati
- **Sensibilità**: Regolabile tramite soglie
- **Cooldown**: 15 frame tra i gesti
- **Precisione**: Sub-pixel per movimenti fluidi

## 🔺 Poligoni Supportati

| Lati | Nome | Simbolo |
|------|------|---------||
| 3 | Triangolo | 🔺 |
| 4 | Quadrato | ⬜ |
| 5 | Pentagono | ⬟ |
| 6 | Esagono | ⬡ |
| 7 | Ettagono | ⬢ |
| 8 | Ottagono | ⬣ |
| 9+ | Poligono N-lati | 🔷 |

## 🔧 Risoluzione Problemi

### Problemi Comuni

**❌ Errore: Webcam non trovata**
```bash
# Verifica dispositivi disponibili
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

**❌ Errore: ModuleNotFoundError**
```bash
# Reinstalla le dipendenze
pip install --upgrade -r requirements.txt
```

**❌ Rilevamento mano impreciso**
- ✅ Migliora l'illuminazione della stanza
- ✅ Posiziona la mano a 30-60cm dalla camera
- ✅ Evita sfondi complessi o in movimento
- ✅ Mantieni la mano ben aperta e visibile

**❌ Lag o performance scarse**
- ✅ Chiudi altre applicazioni che usano la webcam
- ✅ Riduci la risoluzione della webcam
- ✅ Aggiorna i driver della scheda grafica

### Log di Debug

Il terminale mostra informazioni dettagliate:

```bash
INFO: MediaPipe inizializzato correttamente
INFO: Webcam rilevata: 1280x720 @ 30fps
DEBUG: Gesto rilevato: Allargamento - Lati: 5
WARNING: Mano non rilevata per 30 frame
```

## 🛠️ Tecnologie Utilizzate

| Tecnologia | Versione | Utilizzo |
|------------|----------|----------|
| **Python** | 3.8+ | Linguaggio principale |
| **OpenCV** | 4.8+ | Computer vision e GUI |
| **MediaPipe** | 0.10+ | Hand tracking ML |
| **NumPy** | 1.24+ | Calcoli matematici |

### Architettura del Sistema

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Webcam Input  │───▶│  MediaPipe Hand  │───▶│  Gesture Logic  │
└─────────────────┘    │    Detection     │    └─────────────────┘
                       └──────────────────┘             │
┌─────────────────┐    ┌──────────────────┐             │
│  Visual Output  │◀───│  Polygon Render  │◀────────────┘
└─────────────────┘    └──────────────────┘
```

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## 🤝 Contributi

I contributi sono benvenuti! Per contribuire:

1. Fai un fork del progetto
2. Crea un branch per la tua feature
3. Committa le modifiche
4. Apri una Pull Request

---

**Divertiti a controllare i poligoni con i gesti!** 🎉

*Realizzato con ❤️ da @alex1dev*
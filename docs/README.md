# Smol but Mighty: Addestra il tuo Mini Language Model

## Introduzione

Prima di iniziare, è utile capire dove si collocano i modelli linguistici all'interno del panorama dell'Intelligenza Artificiale.

1.  **Intelligenza Artificiale (AI)**: Il ramo dell'informatica che si occupa di risolvere problemi che tipicamente richiedono l'intelligenza umana.
2.  **Machine Learning (ML)**: Un sottoinsieme dell'AI in cui le macchine vengono addestrate tramite esempi noti per renderle in grado di risolvere problemi reali per i quali non sono state programmate esplicitamente.
3.  **Deep Learning (DL)**: Un sottoinsieme del ML che utilizza reti neurali profonde (con molti strati nascosti) per apprendere pattern complessi.
4.  **Transformer**: Un'architettura di Deep Learning, introdotta da Google nel 2017 con il paper "Attention is All You Need". Nata per compiti di traduzione, ha rivoluzionato il campo del Natural Language Processing (NLP) e ha dato vita a modelli come GPT e BERT.

I modelli che andremo ad addestrare sono **Mini Language Models**, ovvero modelli linguistici di piccole dimensioni, basati su architetture Transformer.

## Cos'è un Transformer?

Un Transformer è un **Modello Linguistico**, ovvero una rete neurale addestrata su enormi quantità di testo. Questo addestramento iniziale, chiamato **Pre-Training**, avviene in modalità **Self-supervised Learning**.

- **Self-supervised Learning**: Il modello impara i pattern, la grammatica e le relazioni semantiche del linguaggio senza bisogno di etichette manuali. Una tecnica comune è il _masking_, usata per esempio da BERT. Questa tecnica prevede che una parola in una frase viene nascosta (es. `Il gatto dorme sul [MASK]`) e il modello deve predire la parola mancante (`divano`) basandosi sul contesto.

Il risultato del Pre-Training è un **Pre-trained Model**, un modello con una conoscenza statistica generale del linguaggio, ma non ancora specializzato in un compito specifico.

### Fine-Tuning: Specializzare il Modello

Il **Fine-Tuning** è il processo che adatta un modello pre-addestrato a un compito specifico (es. classificazione del testo, chatbot, traduzione). Questo approccio, noto come **Transfer Learning**, sfrutta la conoscenza generale del modello di base per ottenere ottime performance su un compito specifico con un dataset di addestramento molto più piccolo.

## Smontiamo un Transformer

L'architettura di un Transformer è composta principalmente da due blocchi:

- **Encoder**: Processa la sequenza di input (es. una frase in italiano) e la converte in una rappresentazione numerica che ne cattura il significato.
- **Decoder**: Prende la rappresentazione dell'Encoder e genera una sequenza di output (es. la traduzione in inglese).

L'encoder e il decoder possono essere utilizzati in modalità combinata o separatamente.
Esistono modelli che utilizzano solo l'encoder (es. BERT) e modelli che utilizzano solo il decoder (es. GPT).

Per funzionare, si avvalgono di alcuni componenti fondamentali:

- **Tokenizer**: Suddivide il testo di input in unità più piccole chiamate "token" (parole, sotto-parole o caratteri).
- **Word Embedding**: Converte ogni token in un vettore numerico. In questo "spazio degli embedding", parole con significato simile avranno vettori vicini.

## Tecniche di Fine-Tuning

### 1. SFT (Supervised Fine-Tuning)

È la tecnica base di fine-tuning in cui si addestra ulteriormente un modello pre-addestrato su un dataset etichettato e specifico per il nostro task.

In questa fase, si addestra il modello su un dataset etichettato, in modo che imparino a rispondere in modo corretto alle domande del dataset. Sfruttando però le capacità generali del modello di partenza, bastano relativamente pochi esempi per ottenere ottimi risultati.

### 2. Preference Alignment

Dopo l'SFT, si può migliorare la qualità e lo stile dell'output del modello. L'obiettivo è allineare le risposte del modello alle preferenze umane (es. renderle più formali, più creative, o in un formato specifico come JSON).

Le principali tecniche di _Preference Alignment_ sono:

- **DPO (Direct Preference Optimization)**: Utilizza un dataset di preferenze (prompt, risposta scelta, risposta scartata) per affinare ulteriormente il modello dopo l'SFT.
- **ORPO (Odds Ratio Preference Optimization)**: Una tecnica più recente che combina SFT e DPO in un unico passaggio, rendendo il processo più efficiente.

## PEFT: Fine-Tuning Efficiente

Il fine-tuning tradizionale aggiorna tutti i parametri del modello, richiedendo enormi risorse computazionali (GPU) e di storage, con il rischio di "dimenticare" le capacità generali del modello di partenza (_catastrophic forgetting_).

**PEFT (Parameter-Efficient Fine-Tuning)** risolve questi problemi. Invece di modificare l'intero modello, si interviene solo su una piccola parte dei parametri.

### LoRA (Low-Rank Adaptation)

LoRA è la tecnica PEFT più diffusa. Il suo funzionamento si basa su questi principi:

- **Congela i parametri** del modello originale, che non vengono modificati.
- **Inietta matrici di decomposizione** a basso rango ("adattatori"), che sono piccole e addestrabili.
- **Riduce drasticamente** il numero di parametri da addestrare (fino al 90-99%).

Questo permette di:

- Risparmiare enormi quantità di risorse computazionali.
- Salvare solo i piccoli "adattatori" (pochi MB) invece di intere copie del modello (diversi GB).
- Preservare le capacità originali del modello, evitando il _catastrophic forgetting_.
- Applicare e combinare diversi adattatori a un unico modello base per svolgere compiti differenti.

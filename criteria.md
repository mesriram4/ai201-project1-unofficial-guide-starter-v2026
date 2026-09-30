# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer.

**Why this target:**
<!-- A great way to indicate how well the model searches through information and calculate distance (showcases relevancy of chunks to prompts). A measure of how far a model would go to search for information so long as it corresponds exactly to or is relevant enough to the prompt. -->

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
<!-- MY ANSWER: The objective of this system is to test and prevent hallucinations, even out of scope questions or in-scope questions with lack of info need to references sources to prove the system looked through sources to find the best answer -->

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" — in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- There should be a clean cut gap, where there is little to virtually no overlap in best distances between in-scope and out-of-scope questions. -->

---

## 4. Split chunks into an appropriate size

Split by every three sentences to produce more than 88 chunks that are concise and informative without leaving out relevant information or contain incoherent sentences unrelated to the main point of that chunk. 

<!-- YOU WRITE THIS ONE.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." 
     -->

'''
Target: 
     + Chunks can be of any size so long as they include three sentences. 
     + Average character size for chunks should be around 250 characters.
     + Avoid chunks that are less than 90 characters.
'''

**Why this target:**
'''
Every three sentences on average will include full sentences or elaborations on a single topic. When running the program, there are a total of 110 chunks. While not dramatically more than the initial amount of chunks, these chunks are still capable of being properly referenced when testing questions. 
'''



---

## 5. Threshold limit

The the distance threshold for the model's response (out of 0.6) should be below 0.45. Should pass 3 out of 5 of the questions given when running this program. 

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. 
     -->
     
'''
Target: 
     + 3 out of 5 of the sample questions should be within the starting threshold (0.6), ideally below 0.45. 
     + 4 out of 5 of the sample questions absolutely have to be within 0.6 even if one of them is above 0.45
'''


**Why this target:**
'''
Below 0.45 indicates that the model is properly retrieving chunks that are strongly related to the information needed to answer the prompt. The requirement itself also tests whether it can answer the test questions (varies by levels of specificity or vagueness towards the existing information used to create the chunks). The reason why I will allow for 3 out of 5 of the tested questions to return distances less than or equal to 0.45 is because of the acceptable possibly of an answer returning something althought it is greater than 0.45, especially if the question asked is more vague and requires reaching out to more chunks.
'''

CHANGE TO CRITERIA (NEW CRITERIA): 

The the distance threshold for the model's response (out of 0.7) should be below 0.55. Should pass 3 out of 5 of the questions given when running this program. 

**WHY THIS NEW TARGET (UPDATED FROM PREVIOUS EXPLANATION)**

Below 0.55 indicates that the model is properly retrieving chunks that are strongly related to the information needed to answer the prompt based on the new threshold. The requirement itself also tests whether it can answer the test questions (varies by levels of specificity or vagueness towards the existing information used to create the chunks). The reason why I will allow for 3 out of 5 of the tested questions to return distances less than or equal to 0.55 is because of the acceptable possibly of an answer returning something althought it is greater than 0.55, especially if the question asked is more vague and requires reaching out to more chunks. Additionally, some questions above 0.55 will still return a response referencing proper sources, but the high distance could be an indication of how vague the question itself is.




---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->

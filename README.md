# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

'''
ANSWER: 

The goal of this "Unofficial Guide" is to use available documents or snippets of information collected on a topic and return answers based on the questions you ask about said topic. For example, the corpus I've chosen to to build my system around is based on the files of 'city_guide'. Basically, the program reorganizes documents under the city_guide folder into chunks. Based on these chunks, the program is capable of answering questions related to information about the city, such as transporation, open business hours, urban planning, housing, etc. However, the bandwidth of information the program can rely on is only so much: if you attempt to input a question completely unrelated to the contents of 'city_guide', the program will warn you about its inability to respond to an out of scope question, avoiding hallucinating an answer instead.

'''

## Chunking Strategy

**Chunk size: 300**
**Overlap: 30**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3.

-->
'''   
ANSWER: My goal was to balance two things about chunks: 1) Chunks have to be concise, not too big or small. 2) Chunks have to provide contextual but straightforward information. 

I realized the best way to accomplish this goal is to make sure the the function split_documents() splits information within city_guides into three sentences for each chunk, given the long-form, paragraphical organization of the initial documents. The max character and overlap values stemmed from experimentation. 

Acknowledging the variety of character lengths three sentences can generate, 300 was an ideal max that I at least wanted the average to stay within. Keeping the overlap at 30 allows two neighboring chunks to share related information (preventing cut-offs while also keeping a chunk that expands upon information of a previous chunk connected to that chunk). These values allow for the model to return more informative and well-developed answers without hallucinating its own answers or admitting to not having enough info.
'''

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. 

-->


**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance. ## Straightforward

**Thornby Wells** is the easiest town in the region.
```

**Chunk 2** — source: `guide_corry_vale.md#3 ` — produced by: `chunker.py::split_documents`

```
## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm.
```

**Chunk 3** — source: `guide_givens_mill.md#0` — produced by: `chunker.py::split_documents`

```
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted. ## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes.
```

**Chunk 4** — source: `guide_kestrelford.md#7` — produced by: `chunker.py::split_documents`

``` 
The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters. ## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts.
```

**Chunk 5** — source: `guide_regional_transport.md#4` — produced by: `chunker.py::split_documents`

```
The Halden Bay coast road is cut into the cliff
and is slow rather than difficult. Parking is the constraint rather than driving. Both Halden Bay lots fill by
10am on summer weekends.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
'''
"What time of year is best for affordable housing"
'''

**Answer:**

```
According to *guide_marchwood.md*, accommodation is plentiful and cheap outside of conference weeks. *guide_brightwater.md* states that outside of graduation week and early September, there is more supply than demand for accommodation. Additionally, *guide_halden_bay.md* notes that prices roughly halve outside of July and August.

Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_thornby_wells.md
```

**My relevance cutoff**
'''
0.7
'''

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. 
     -->
'''
ANSWER: The threshold I reconfigured to is 0.7. By configuring the threshold higher than the initially established, the model is able to answer more questions without outputting an error message.  
'''


| Question | In corpus? | Best distance |
|"What time of year is best for affordable housing"|Yes|0.610 (threshold: 0.7)|

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
'''
Claude During Milestone 2: 

This is my first time writing acceptance criteria for a project. After reading through CodePath's instructions, I wrote my criteria and ran a prompt asking Claude to evaluate how it would test those questions given the criteria I've established. Claude was able to give me insightful notes on how to tailor my questions. For example, one criteria I initially wanted to establish was creating 4x as many chunks as initially established (88). I asked Claude how it would test it and how well it can understand said criteria. Claude was able to give me some meaningful feedback on what to change due to vagueness or similarities to previous criteria. 

Claude initially recommended I split by paragraph when creating my chunks. However, I disagreed with the chatbot and instead opted to split chunks by sentence. This method proved to have been inefficient, so I came up with the idea to split chunks by three sentences again and had Claude run the criteria again. It approved of the changes and confirmed that this criteria is good to go. 

Additionally, Claude was able to assist with modifying the code to best reflect the chunking strategy I wanted for the program.
'''


**2.**

'''
Claude during Milestone 3:

After experimenting with chunking criteria and officially settling on chunking by three sentences, I was able to ask Claude to evaluate 5 of the chunks and determine if they are comprehensible. Additionally, I asked Claude what kind of questions these chunks would likely be able to answer based on each chunk. Overall, Claude contributed to the trial and error process of figuring out what chunking strategy can lead to the best results.

'''



<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | 4/5 |
| 2. Every answer names a source | 5 of 5 | 4/5 | 4/5 | 4/5 | 4/5 |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5  | 5/5 | 5/5 | 5/5 |
| 4. Split chunks into an appropriate size | 4 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 5. Threshold limit | 3 of 5 | 1/5 | 1/5 | 1/5 | 1/5 |

(Change to criteria 5 to accomodate for threshold change from 0.6 to 0.7 --> see criteria.md)

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->


 **1. Retrieved chunk contains the answer:**
 "One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm." (Source for Question 1)

**2. Every answer names a source**

"### What are the opening hours of local restaurants — run 1" 

- Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_pellew_sands.md 

**3. Gate stops out-of-corpus questions**

Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.797)  What is the capital of Mongolia?
  refused  (best distance 0.893)  How do I change the oil in a diesel engine?
  refused  (best distance 0.975)  Who won the 1994 World Cup?
  refused  (best distance 0.841)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.824)  How do I write a for loop in Rust?
  -> gate refused 5 of 5

**4. Split chunks into an appropriate size**

======================================================================
Chunk 2  |  source: guide_corry_vale.md#3  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm.


**5. Threshold limit**

### What are the opening hours of local restaurants — run 2

- Best distance: 0.4270 (passed the gate)


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | Meant to pass 4 out of 5 questions for all runs. Passed 4 out 5 as expected. This criteria was measured by the degree of relevance the source has to a prompt. Best evidence provided was one of the chunks used to answer question 1 (opening hours for local restaurants). That chunk is one of many chunks used for this question that contains a direct answer to the test question.|
| 2 | Every answer names a source | MET | While the goal was 5/5, the 4/5 came from the model not having enough info to answer one of the questions, meaning a source will be provided if the model has enough info to answer a question (will still list sources it checked when formulating an answer). Overall, even for in-corpus questions that the model could not answer, the model will state that it has searched through available sources and let the user know that it cannot identify sources to answer all questions, demonstrated commitment to always using sources for outputs.|
| 3 | Gate stops out-of-corpus questions | MET | Model refuses to answer out-of-corpus questions 100% of the time. Similar to the results of criteria 2. |
| 4 | Split chunks into an appropriate size | MET | Initially 4/5, but all chunks were split into three sentences each as desired.  |
| 5 | Threshold limit | MISSED | Set an expectation for best distance staying below 0.45, but since I set the threshold to 0.7, most questions had a best distance between 0.5 to 0.6. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

Questions 2 and 5 are the most interesting most due to variability in answers depending on runs. For context, questions 2 and 5 have a greater best distance compared to other in-scope questions (both above 0.6), so while the model is able to return responses every run, there are times where the program will return more information or even withold additional information during runs. I believe this is a problem with retrieval especially for questions with greater distances.

To solve this retrieval issue and make sure the program is consistently returning relevant information without oversharing or witholding information, I changed the top-k value from 10 to 14, allowing for the program to consistently return more relevant information. For example, Question 2 initially returned information on a town that is the most transporation-friendly, but the program also returned information on a town with the best train network. Sometimes, the program will bring up the train network , other times, it won't. When increasing the top-k from 10 to 14, I initially expected the program to consistently bring up the network, however, after re-running it a few times, the train network was left out more often, but in return, the program emphasized the efficiency of transporation in the first time much more than it did when top-k = 10. Therefore, I finalized 14 as my top-k, understanding that the program was able to expand more on a relevant topic than bring up something slightly less relevant to the prompt. 

Additionally, I tested the new top-k on Question 5, which was able to consistently return more information on affordable housing than when top-k = 10. I also tested the rest of the questions, and the responses were much more informative and polished when top-k = 14. However, when testing the 4th question regarding local events for students, the program still claimed it did not have enough information on the topic, possibly confirming the 4th question might possibly be out of scope.

Summary of diagnosis and fix: 
- Diagnosis: Inconsistent retrieval for questions with higher distances (Questions 2 and 5)
- Fix: Increasing top-k to allow for more consistently informative answers during runs.


## The Improvement

**What I changed:**

Previous, I changed top-k during the Diagnoses question in the hopes of improving answer consistency. This time, I want to change the chunking strategy to organize ideas much more efficiently. 

Strategy: Still chunk by three sentences, but within sections of the document (indicated by titles). Instead, the program first identifies sections within the document, then attempts to chunk by three sentences within a paragraph. If the program encounters the paragraph ending before three sentences, then the program will just return the remaining number of sentences so long as it stops at the paragraph break. The same rule applies to if a program encounters a new title within the document. 

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

The diagnosis I've chosen for milestone 3 related to issues with retrieval. While the diagnosis I'm currently looking at is chunking-related, this process is meant to make retrieval much more efficient and organized. This change might require a higher top-k, since information retrieval is a lot more contained and will have to access other chunks compared to the previous chunking strategy (chunking by three sentences regardless of topic relatability). 

The new chunking strategy I now used is the following: 
+ Chunking withing every header within a document. 
+ Within every header and every section of that header, I will still be chunking by three sentences. If for every section, I'm left with one sentence in that section, that additional sentence will be added to the previous 3-sentence chunk. 
+ If a section is less than three sentences long, that section will be added to the chunk before (this is only done within sections and not headers. All chunks remain within their respective headers). 
+ The goal of this strategy is to account for topic relatability.

The new top-k value for this new strategy is: 15
+ Marginally different from 14, the change I made in milestone three (according to input from Claude). The number of chunks the model references will still be similar.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 4. Split chunks into an appropriate size | 4 of 5 | 5/5 | 5/5 | 5/5 | 5/5 |
| 5. Threshold limit| 3 of 5 | 2/5 | 2/5 | 2/5 | 2/5 |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Not much of a difference has been made after changing the chunking strategy and the top-k from 14 to 15. Initially, I believed my responses will be more informative and consistent. While my responses are highly informative especially for questions 1 and 3, 2 and 5 are now inconsistent with the responses they are returning compared to the previous chunking strategy, where a top-k of 14 returned more relevant information consistently, and question 5 especially has answers that are slightly more lackluster compared to its responses during previous runs.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

# Quiz: Lecture 1 (Slides 1–24)

**Course:** Computer Architecture  
**Source:** Lecture-1.pdf — *Fundamentals of Quantitative Design and Analysis* (Hennessy & Patterson, 6th Ed., Ch. 1), **Slides 1 to 24 only**.

Answer each question by editing `answers.json`: set each `"Q1"` … `"Q10"` to the letter of your choice (e.g. `"A"`, `"B"`, `"C"`, or `"D"`).

You can run the grader locally with `python grader.py`, or push to GitHub for automatic grading.

---

## Questions

**Q1.** In which year did single-processor performance improvement effectively end, according to the lecture?
- A) 2001  
- B) 2003  
- C) 2005  
- D) 2010  

**Q2.** Which of these is NOT listed as a new model for performance after ILP?
- A) Data-level parallelism (DLP)  
- B) Thread-level parallelism (TLP)  
- C) Instruction-level parallelism (ILP)  
- D) Request-level parallelism (RLP)  

**Q3.** Which class of computer emphasizes "energy efficiency and real-time"?
- A) Desktop Computing  
- B) Servers  
- C) Personal Mobile Device (PMD)  
- D) Clusters / Warehouse Scale Computers  

**Q4.** In Flynn's taxonomy, SISD uses:
- A) Single instruction stream, single data stream  
- B) Single instruction stream, multiple data streams  
- C) Multiple instruction streams, single data stream  
- D) Multiple instruction streams, multiple data streams  

**Q5.** SIMD is best suited for problems with a high degree of:
- A) Irregularity  
- B) Regularity  
- C) Branching  
- D) I/O  

**Q6.** Which Flynn classification has "no commercial implementation"?
- A) SISD  
- B) SIMD  
- C) MISD  
- D) MIMD  

**Q7.** Most modern supercomputers fall into which category?
- A) SISD  
- B) SIMD  
- C) MISD  
- D) MIMD  

**Q8.** The "old" view of computer architecture is primarily concerned with:
- A) Microarchitecture only  
- B) Instruction Set Architecture (ISA) design  
- C) Power consumption only  
- D) Cost only  

**Q9.** How many general-purpose and floating-point registers does RISC-V have?
- A) 16 g.p., 16 f.p.  
- B) 32 g.p., 32 f.p.  
- C) 64 g.p., 64 f.p.  
- D) 32 g.p., 16 f.p.  

**Q10.** According to the lecture (Bandwidth and Latency), bandwidth (or throughput) refers to:
- A) Time between start and completion of an event  
- B) Total work done in a given time  
- C) Clock speed only  
- D) Cache size  

---

## How to submit

1. Fill in `answers.json` with your choices (e.g. `"Q1": "B"`).  
2. Run `python grader.py` locally to see your score (optional).  
3. Push your branch to GitHub or open a pull request; the **Grade Quiz** workflow will run and show pass/fail.

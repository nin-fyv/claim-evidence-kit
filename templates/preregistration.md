# Pre-registration: [short name of the test]

**Written:** [date] · **Owner:** [name] · **Frozen before any result is seen:** yes / no

## 1. The question
One sentence. What are you trying to find out?

## 2. What is being tested
The version, configuration or change under test, exactly enough that someone else could rerun it.

## 3. The measure
- **Primary measure:** [what you count or compute]
- **How it is computed:** [formula or procedure]
- **Data:** [which data, how it was chosen, and that it was not used to build what is being tested]

## 4. The pass bar
- **Pass if:** [the threshold, stated before running]
- **Fail if:** [what result would show it does not work]
- **Inconclusive if:** [too little data, a broken run, and so on]

## 5. What this will and will not allow you to say
- If it passes, the most you may say is: "[sentence]"
- It will not support: [claims that would go beyond the test]

## 6. Things that could fool you
Leakage between build and test data, picking the best of many runs, changing the bar afterwards, a small sample.

## 7. Changes after freezing
Any change made after this was frozen is listed here with the date and the reason. The original text above is not edited.

| Date | Change | Reason |
|---|---|---|

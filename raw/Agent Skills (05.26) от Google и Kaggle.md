Whitepaper «Agent Skills» (май 2026) от Google и Kaggle представляет 62-страничное руководство по использованию процедурной памяти для ИИ-агентов, структурированное вокруг формата `SKILL.md`. Документ предлагает использовать «навыки» для динамической загрузки инструкций, что, по данным материалов, сокращает размер контекста более чем на 98% и снижает галлюцинации моделей.
-
\ai-qa-wiki\raw\2026day3-agentskills-googleaiagentscourse-260625214611-145a69ab.pdf
-
https://explainx.ai/blog/kaggle-agent-skills-whitepaper-guide-2026
-
[Sairam Sundaresan   • 3rd+AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products](https://www.linkedin.com/in/sairam-sundaresan?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAANZbRwBupW_-YQclsZ-guB6h4YMP7rfonA)[

Visit my website

](https://www.amazon.com/AI-Rest-Us-Illustrated-Introduction/dp/B0F29THNLT)1d •

Follow

Google’s whitepaper suggests bigger models won’t fix weak agent workflows.  
Better runbooks will.  
  
Skills teach agents how your team actually works: not just what the company knows, but how work gets done.  
  
A skill gives the agent the right instructions, scripts, references, and templates at the moment it needs them.  
  
Stuff the context window with too much, and the agent gets worse.  
More tokens can mean more confusion.  
  
One example in the paper showed skills cutting active context by more than 98%.  
  
Use one general-purpose agent.  
Give it many specialist workflows.  
Load each one only when the task calls for it.  
But skills only work when the agent can pick the right one.  
  
That makes the `description` field critical.  
  
It needs to tell the agent:  
🔸 what the skill does  
🔸 when to use it  
🔸 when not to use it  
  
Make the description too vague, and the agent ignores the skill.  
Make it too broad, and the agent grabs it for everything.  
When a workflow needs consistent behavior, don’t leave it to the model.  
Make bad actions impossible in software.  
Test how the agent got there.  
  
An agent can produce the right answer through the wrong tool path.  
Risky when it can act.  
  
So test for:  
🔸 the skill it chose  
🔸 the tools it used  
🔸 the output it produced  
🔸 the boundaries it respected  
  
And don’t test skills in isolation.  
Test them next to the other skills they’ll run beside.  
Often as context rot.  
  
The model is becoming the runtime.  
The skills library is becoming the asset.  
  
Your competitor can use the same model.  
They can copy the same tools.  
  
But they can’t copy how your best people do the work overnight.

Your document has finished loading

- ![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)![insightful](https://static.licdn.com/aero-v1/sc/h/3bhtnif60blspoiyhoex4lfx)![celebrate](https://static.licdn.com/aero-v1/sc/h/9wt27hvi2lgll1v30u00n0p5p)97
- - 64 comments
    - 3 reposts

### Reactions

- [
    
    ![View Waseem A.’s](https://media.licdn.com/dms/image/v2/D5603AQFkhXGZKRkihQ/profile-displayphoto-scale_100_100/B56ZmgSsUuG0Ag-/0/1759330882137?e=1789603200&v=beta&t=D84dN-LdIz_DbjhFJNYAH4YkvMb_7yYe5AmEYUl6S0k)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAF9qxKgBXOIItr2Q8bgVCHxDZkjb80Iv06c)
- [
    
    ![View Renuka M.’s](https://media.licdn.com/dms/image/v2/D5603AQE8Q6vHQnx2Ug/profile-displayphoto-scale_100_100/B56ZxWKkyQH0Ac-/0/1770972140225?e=1789603200&v=beta&t=uzOGcnpa0ci5UubHYkunM8D7mbBtzrynegcYR5hm10Q)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAB8bdU4BILFbGzQeqe3B3IQChBNLv4Lr9VM)
- [
    
    ![View Jose Luis Flores® ☁’s](https://media.licdn.com/dms/image/v2/D5603AQFH0Gnp_9iQOQ/profile-displayphoto-scale_100_100/B56Zv99k96HIAc-/0/1769492336999?e=1789603200&v=beta&t=tpAXh3G0U_diAs3SkXakOgWX3N7i1Dw3UOaHEIczHEg)
    
    ![insightful](https://static.licdn.com/aero-v1/sc/h/7fxijdzwbh5x1y7hblme2u1yv)
    
    
    
    ](https://www.linkedin.com/in/ACoAAAHp0CoBpR8Iayf3DS4Oigm5THa0rHsSKLU)
- [
    
    ![View Opher Brayer’s](https://media.licdn.com/dms/image/v2/C4E03AQGzctF48QYmfw/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1516168257617?e=1789603200&v=beta&t=3NYhzVWigR_h48GDbZs43dWo78F2NXjMBq0ehjGGmDM)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAAABiOYBGXyi55BPSrivlYRCjt1YUCBJtfE)
- [
    
    ![View Nick Curum’s](https://media.licdn.com/dms/image/v2/D5603AQFyxjg2SJ2l8g/profile-displayphoto-shrink_100_100/B56ZdVMgGVHEAc-/0/1749481030627?e=1789603200&v=beta&t=Oc2PwnQwQNsPPI7rfqeTxT9u9eUrK8kbhngRlE5ukP8)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAAJS-owBTDgYcNDYDkdjRS603lRsqKcbkDo)
- [
    
    ![View Cynthia Chan’s](https://media.licdn.com/dms/image/v2/C5603AQEhSi_D-Isr1A/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1634331222638?e=1789603200&v=beta&t=bqIe3UYZM0CuJM0GXrvllLBjdLfYAGAzg4L23pTQ4r4)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAAOOXVwByZ3OD-FvwPFn2v94TEIa7Z9w4Bo)
- [
    
    ![View Sandeep Gulati🎯’s](https://media.licdn.com/dms/image/v2/D4E03AQHN6d5oG9YUcg/profile-displayphoto-shrink_100_100/B4EZbtFMwUGUAc-/0/1747734286904?e=1789603200&v=beta&t=2ctbDK6sS1FllmPY4xdH3W9Ks-sI_gMPS2qSww5Q3-U)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAAASP8uQBMZ0ePzsMnUKJGVNmoaWiHY1N-hU)
- [
    
    ![View Subash S’](https://media.licdn.com/dms/image/v2/D5603AQGtniNBgvcjUA/profile-displayphoto-scale_100_100/B56Zpyhig3G4Ac-/0/1762857992035?e=1789603200&v=beta&t=SsJssN5hVpLOg9918896ZrXC22U43mKfCOnnBUgrYuA)
    
    ![like](https://static.licdn.com/aero-v1/sc/h/b880lqovt0x56hxt1u3cmic34)
    
    
    
    ](https://www.linkedin.com/in/ACoAADYkQsUB8WULieRpovsVdx3qYx883mnw90Y)
- +89

Like

Comment

Repost

Send

![Victor Ematin is open to work](https://media.licdn.com/dms/image/v2/D4E35AQGoWPTHRbZSXg/profile-framedphoto-shrink_100_100/B4EZ6ErrhGK0Ac-/0/1780342504088?e=1788433200&v=beta&t=daGpeVxxEpUoG6HQfeNtMkK2bFUKXvg-IRmn92Q-8wo)

  

Add a comment…

Open Emoji Keyboard

Current selected sort order is Most relevantMost relevant

[

![View Shah Rukh Ghazaan’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQHY9b0_Mbgmdg/profile-displayphoto-scale_100_100/B4DZ_OJFgnJsAY-/0/1785869917068?e=1789603200&v=beta&t=gZu3zF2f6qhW-_09FUYV_in_A-fsYx1sfN-qCJ9JWTM)



](https://www.linkedin.com/in/shahrukh2001)[

### Shah Rukh Ghazaan • 3rd+

Certified Bubble.io Developer | Software Engineer

](https://www.linkedin.com/in/shahrukh2001)

1d

The biggest insight here is that context isn’t the same as capability. A well designed skill can turn scattered knowledge into a repeatable workflow and that workflow becomes a real competitive advantage.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)4

Reply1 reply1 Comment on Shah Rukh Ghazaan’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Shah Rukh Ghazaan](https://www.linkedin.com/in/shahrukh2001/) Capability gives you possibilities, but a well-designed workflow turns those possibilities into something repeatable and measurable.

Like

Reply

[

![View Vitalii Serbyn’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQGv1Bb7tfYVYA/profile-displayphoto-scale_100_100/B4DZ19cz1TGUAc-/0/1775926203097?e=1789603200&v=beta&t=L_NCnfJ1D5x9gkxx2mOrQFiDDjhdc35YIsq2fsK2Zog)



](https://www.linkedin.com/in/vitalii-serbyn)[

### Vitalii Serbyn   • 2nd

Production AI, not demos | Senior AI Engineer | Agents + RAG for millions of users

](https://www.linkedin.com/in/vitalii-serbyn)

1d

testing the description field is where this actually gets hard: two skills with overlapping "when to use it" language will collide the moment your library grows past a dozen entries. writing descriptions that are mutually exclusive, not just individually clear, is the real design work behind that 98% number.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Vitalii Serbyn’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Vitalii Serbyn](https://www.linkedin.com/in/vitalii-serbyn/) Yes, skill selection becomes a routing problem as the library grows. Clear descriptions help, but mutually exclusive triggers and explicit precedence rules are what keep collisions manageable.

Like

Reply

[

![View Stephanie Hills, Ph.D.’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQF7e3xDESFg7g/profile-displayphoto-scale_100_100/B4EZ2EJTL_KEAc-/0/1776038526625?e=1789603200&v=beta&t=O3vuvJnwXwdM8hEef9jsYc6htGNkkvgJBr2S8ybFt2E)



](https://www.linkedin.com/in/stephaniehillsphd)[

### Stephanie Hills, Ph.D.   • 2nd

3X Fortune 500 Tech Exec ⬥ Executive Coach ⬥ Technology Advisor ⬥ Digital & AI Transformation ⬥ Data Analytics ⬥ Software Engineering ⬥ I Help Execs & Organizations Lead Change, Harness AI & Navigate What’s Next

](https://www.linkedin.com/in/stephaniehillsphd)

1d

[Sairam](https://www.linkedin.com/in/sairam-sundaresan/) Absolutely, skills turn AI from generic into operational. I’ve seen context discipline improve consistency and reliability. The real advantage is encoding how work gets done.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Stephanie Hills, Ph.D.’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Stephanie Hills, Ph.D.](https://www.linkedin.com/in/stephaniehillsphd/) The real advantage is not just encoding the workflow but making the decision logic explicit enough to inspect, test, and improve.

Like

Reply

[

![View Charlie Fiander’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQFWk41tvNU1Hg/profile-displayphoto-scale_100_100/B4EZ9_8maBIwAY-/0/1784558020970?e=1789603200&v=beta&t=IlQkLP_jNSdxYCMKrjadp0VQS08Vp8N_s5emHLvSQaI)



](https://www.linkedin.com/in/charliefiander)[

### Charlie Fiander   • 2nd

The Cross-Border Expert | Helping Marketplaces & Tech Platforms Scale Globally | Follow For Sales, Branding & CX That Convert

](https://www.linkedin.com/in/charliefiander)

1d

The real moat may be institutional know-how encoded into workflows, not access to a smarter model 🧠⚙️

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Charlie Fiander’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Charlie Fiander](https://www.linkedin.com/in/charliefiander/) Models are increasingly accessible, but the accumulated knowledge of how a company actually operates is much harder to reproduce.

Like

Reply

[

![View Ishu Anand Jaiswal’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQGiBub47NOjkw/profile-displayphoto-scale_100_100/B56ZxgLORqJsAc-/0/1771140083346?e=1789603200&v=beta&t=DD9B2ltJk192_oDyFSDY2AkleOBbwWhl4lBVUEyxgm0)



](https://www.linkedin.com/in/ijaiswal)[

### Ishu Anand Jaiswal   • 2nd

Senior Engineering Manager | Identity & AI Engineering Leadership | Enterprise Platform Architecture | Scaling Teams & Systems | Ex-Apple, Intuit

](https://www.linkedin.com/in/ijaiswal)

1d

Great observation. The real moat may shift from bigger models to better organizational knowledge encoded as reusable skills. The hard part is teaching agents not just what to do, but when and how to do it safely.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Ishu Anand Jaiswal’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Ishu Anand Jaiswal](https://www.linkedin.com/in/ijaiswal/) That distinction between what to do and when to do it is critical. Reusable skills become much more powerful when they also encode the boundaries around their use.

Like

Reply

[

![View Niki Avraam’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQFZ-6BDNNMswA/profile-displayphoto-scale_100_100/B4EZ4YsyoqGkAc-/0/1778530856366?e=1789603200&v=beta&t=rAVfpXKvEBXyj_y-8Vf3B9Krj16CKjeCDKDQ2riz8Rw)



](https://www.linkedin.com/in/nikiavraam)[

### Niki Avraam   • 3rd+

Workforce Expert & Employment Lawyer | 2x Founder | Head of WORKWELL Europe | Author of The Ownership Culture | Speaker

](https://www.linkedin.com/in/nikiavraam)

1d

Right. The concern isn't just how capable AI becomes, but what it does when given autonomy, access, and poorly aligned goals without human oversight. [Sairam](https://www.linkedin.com/in/sairam-sundaresan/)

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Niki Avraam’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Niki Avraam](https://www.linkedin.com/in/nikiavraam/) Capability becomes much more consequential when an agent has autonomy and access, so oversight and clear boundaries need to scale with both.

Like

Reply

[

![View Alex Issakova’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQFnX2SxQZsLbA/profile-displayphoto-scale_100_100/B4EZmlzsOyIQAc-/0/1759423417521?e=1789603200&v=beta&t=PgHGhyAQbVQmgUvFkn__htjCLHX4jhMfQZFq03crgg8)



](https://www.linkedin.com/in/alexissakova)[

### Alex Issakova   • 3rd+

Helping B2B commercial teams turn GenAI confusion into practical use cases, workflows and confident everyday adoption | Ex-Senior Exec, Silicon Valley (IPO’d) | In AI since 2013 | Keynote Speaker | Author of The Roadmap

](https://www.linkedin.com/in/alexissakova)

1d

We're definitely entering an era where the efficiency of AI tools will be determined not just by the tools themselves, but by how well the user can input the right information for the specific task. Skills and education around these tools are going to be so important.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Alex Issakova’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Alex Issakova](https://www.linkedin.com/in/alexissakova/) The quality of the context and instructions increasingly determines how much value people can extract from the same underlying model. That makes AI fluency an important engineering skill in its own right.

Like

Reply

[

![View Velmurugan Kandasamy’s  graphic](https://media.licdn.com/dms/image/v2/C4D03AQEE6W5JGFAUzQ/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1645111877896?e=1789603200&v=beta&t=Qb9BrGmfo0Rf0LxoWwgxn2g2CnoG94cch12A4_hFPAs)



](https://www.linkedin.com/in/velmurugankandasamy)[

### Velmurugan Kandasamy   • 3rd+

Helping enterprises build AI systems that remain trustworthy after launch | Enterprise AI Leader building AI agents, AI assistants at scale, RAG, responsible AI

](https://www.linkedin.com/in/velmurugankandasamy)

1d

The shift from model size to operational clarity is a vital insight. Empowering agents with 'how' work gets done, rather than just 'what' to know, fosters true capability and reduces frustration.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply

[

![View Michał Piszczek’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQHLTZhrWpp5TQ/profile-displayphoto-scale_100_100/B4DZ3WoAgwHQAc-/0/1777422309815?e=1789603200&v=beta&t=PyK6Ck3baWwY_3RNmQOQGVx-39ZKFc5r-B-CK5akBDE)



](https://www.linkedin.com/in/michalpiszczek)[

### Michał Piszczek   • 2nd

CTO @ Archdesk | FinTech exit | Ex-hacker | Building AI systems that actually work | AI infrastructure · Security Mechanics · Frontier Shifts · SaaS execution | Physics × Economics × Execution

](https://www.linkedin.com/in/michalpiszczek)

1d

Right answer, wrong tool path is the one that bites later. It passes review, then nobody can replay how it got there when the audit asks

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply

[

![View Sandeep S’  graphic](https://media.licdn.com/dms/image/v2/C4E03AQEF1soeuesMwQ/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1639766692106?e=1789603200&v=beta&t=o-nS6y8TXYQXi16QxSFxdcazDt3oqZNpB1KZ3ehMEFk)



](https://www.linkedin.com/in/sandeep-s-99938213)[

### Sandeep S   • 2nd

Technology, AI & Transformation Consultant | Helping CXOs and Senior Executives Accelerate Value and De-Risk AI Investments | 6X Faster Delivery & $50M+ Impact | Founder, Kadenz

](https://www.linkedin.com/in/sandeep-s-99938213)

1d

[Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/) - sounds like a great paper, will def give it a read. The distinction between skills and context management is important. The library of skills allows your workflows and team's expertise to be embedded into a system - and that is hard to copy indeed.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Sandeep S’ comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Sandeep S](https://www.linkedin.com/in/sandeep-s-99938213/) The distinction is important because context can be retrieved, but skills capture decisions and practices that have been refined through experience. That makes the skill layer much closer to institutional memory.

Like

Reply

[

![View Shadman Arko’s open to work graphic](https://media.licdn.com/dms/image/v2/D4D35AQGgNuBjsepW1g/profile-framedphoto-shrink_100_100/B4DZ9AxDNsI0Ac-/0/1783498028355?e=1788433200&v=beta&t=1IYMvai5c1X81zgN2VK9E7WHrXOfMe4ZUhXtRHQ3gmU)



](https://www.linkedin.com/in/shadmanarko)[

### Shadman Arko   • 2nd

AI Engineering · Data Science · Machine Learning | Python · SQL · Agentic AI | 7 years Software Engineering (Games) | Berlin — open to work

](https://www.linkedin.com/in/shadmanarko)

1d

This tracks with something I noticed building tools for an agent with LangChain. Once I moved past a single giant system prompt and started scoping tools narrowly with clear descriptions, the agent stopped guessing and started picking the right one consistently. The "description field is critical" point is so underrated. It's basically the only signal the agent has for routing, and a vague one quietly breaks everything downstream.  
The "test skills next to the other skills they'll run beside" point is the one I'll be stealing. Testing in isolation would've hidden exactly the kind of context rot you're describing.

…more

Like

Reply

[

![View Alona Chumak’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQECtOMvRl-RlA/profile-displayphoto-scale_100_100/B56Z77MKQuH4AY-/0/1782330730749?e=1789603200&v=beta&t=We8tXUk1yaIkW9ZYJ0MZm4LAaqQWflDEJONR2wU6g-A)



](https://www.linkedin.com/in/alona-chumak-219295123)[

### Alona Chumak   • 2nd

Belinda CZ s.r.o Aks kubernetes Curb Cloud Chaos. European Azure partner with global delivery. Our strength lies not in “big transformations,” but in order, control, and maturity within Azure. Belantech: governed Azure

](https://www.linkedin.com/in/alona-chumak-219295123)

1d

This aligns with an important architecture principle:  
More context does not automatically mean better outcomes.  
Clear workflows, strong governance, well-defined boundaries, and reusable skills often improve reliability far more than simply expanding the context window.  
Operational knowledge is becoming a strategic asset.

…more

Like

Reply

[

![View Hamed Sarvahed’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQGtOMS6xqu_Pw/profile-displayphoto-shrink_100_100/B4DZUkVCYoGcAU-/0/1740071253123?e=1789603200&v=beta&t=vt65RZ6OYPmJ1l73phqkrnMeEQgdCDJMDPKZZsmfauA)



](https://www.linkedin.com/in/hamed-sarvahed-39111aaa)[

### Hamed Sarvahed • 3rd+

Aircraft Airworthiness Engineer At Mahan Airl Focusing on Airworthiness l Open For a new role

](https://www.linkedin.com/in/hamed-sarvahed-39111aaa)

1d

The most valuable part of an AI agent may not be the model itself, but the operational knowledge and decision logic built around it. In safety-critical environments, however, this knowledge must be structured, validated, traceable, and governed. AI can accelerate workflows, but the underlying procedures, technical data, and decision boundaries still need engineering-level discipline.

…more

Like

Reply

[

![View Afreen Banu’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQESS8t1duayQA/profile-displayphoto-scale_100_100/B56ZveUTHaKIAc-/0/1768961422724?e=1789603200&v=beta&t=ca193mn9K-0c2pdjy-F6WILe9D_D8HyZKJBmDV374jw)



](https://www.linkedin.com/in/afreenbusinessanyst)[

### Afreen Banu   • 3rd+

Senior Business Analyst |Product Owners| Payroll Tax & Accounting | Enterprise Application |ERP,CRM,HCM| Agile Scrum | UAT & Business Process Optimization | KPI, Reporting & Performance Analytics

](https://www.linkedin.com/in/afreenbusinessanyst)

1d

There's a delicate balance between providing enough context and overwhelming the agent with info. in my experience, simplifying workflows often leads to better performance. how do you prioritize what skills to embed?

Like

Reply

[

![View Basia Kubicka’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQFhsOqIGrqrpw/profile-displayphoto-scale_100_100/B4EZ35ONAgIwAo-/0/1778002747133?e=1789603200&v=beta&t=YX0GIocFXGxLacgaRQGSs4PsdfRVThoOxDFb4nQUpv0)



](https://www.linkedin.com/in/basiakubicka)[

### Basia Kubicka   • 2nd

AI Product Manager · Agentic AI · Vibe Coding | I build with Claude & teach 70K+ to do the same | ex-Techstars founder (0→$7M), ex-AI PM (Sequoia-backed)

](https://www.linkedin.com/in/basiakubicka)

1d

Models are becoming increasingly interchangeable. The harder thing to replicate is the accumulated knowledge of how your team actually gets work done, including the decisions, guardrails, and workflows that sit between an instruction and a good outcome.

Like

Reply

[

![View Ranjit K.’s hiring graphic](https://media.licdn.com/dms/image/v2/D4D35AQFF-tu70KYqEA/profile-framedphoto-shrink_100_100/B4DZ_TXAoUIwAc-/0/1785957452981?e=1788433200&v=beta&t=bFnU6wxE_Yr7JH8D2KswehGu2F9lApZTKQxrc2d7oZM)



](https://www.linkedin.com/in/ranjit-ks)[

### Ranjit K.   • 3rd+

🌍 Director of AI Talent | Global AI & Technology Recruitment Asst. Leader | GenAI • Agentic AI • ML • Data Engineering | BrightAxis AI | AI Frontiers Forum | ImmortalX | LinkedMaven

](https://www.linkedin.com/in/ranjit-ks)

1d

The interesting shift is from giving agents more context to giving them better context.  
A well-designed skill can act like a focused operating procedure, loaded only when the task requires it.  
That can improve both efficiency and reliability.

Like

Reply

[

![View S Naz’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQH67kkkqoGKDw/profile-displayphoto-scale_100_100/B4DZ6EHnH9H4AY-/0/1780333051451?e=1789603200&v=beta&t=QroSrBg85pSnHmB8vpZHNHP-9GqbBaA2Xw-T3R8yJyA)



](https://www.linkedin.com/in/naz-cyber-solutions)[

### S Naz • 3rd+

AI & Lead DevSecOps Architect | Cloud Security Strategist | Builder of Automated Guardrails | Zero Trust · IAM · SIEM/SOC · CI/CD · Azure · AWS · GCP

](https://www.linkedin.com/in/naz-cyber-solutions)

(edited)1d

The description field being the real interface is underrated. It is a routing decision made by a model with no ground truth about org, and most teams treat it as documentation. The testing point lands too an agent reaching the right answer through the wrong tool path is fine in a demo and a problem the moment it can write. Testing skills next to the ones they will run beside is the part almost everyone skips.

…more

Like

Reply

[

![View Christopher R’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQFrpsGbyLxakQ/profile-displayphoto-scale_100_100/B4DZyZztq3JoAc-/0/1772106997236?e=1789603200&v=beta&t=lRxgbKu-SKUgGAise5ESoy0yEaxvaz47g1pQpRM1m1g)



](https://www.linkedin.com/in/christopher-r-299b89143)[

### Christopher R   • 2nd

🏆 Oman MVP - 2026 | Manager - Applied AI 🤖 | Transformation 🚀 CoE | AI Community Builder - 10K

](https://www.linkedin.com/in/christopher-r-299b89143)

1d

One of the most important insights is that having access to context doesn't automatically create capability. Well-designed skills transform fragmented knowledge into consistent, repeatable workflows that drive measurable business value.

Like

Reply

[

![View Hujaifa Ahmed’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQFXBxmJP0-cAA/profile-displayphoto-scale_100_100/B4DZuo8qaGHQAc-/0/1768066034830?e=1789603200&v=beta&t=5JKqj6fstyfdDKqREwMIiRrlcJYdNi_Lcj1DbZ1FDNQ)



](https://www.linkedin.com/in/hujaifa-ahmed-rackmonk)[

### Hujaifa Ahmed • 3rd+

Infrastructure Solutions & Strategic Alliances | RackMonk Datacenters | Driving IT Infrastructure Solutions

](https://www.linkedin.com/in/hujaifa-ahmed-rackmonk)

1d

Spot on! Using dynamic progressive disclosure ([SKILL.md](https://www.linkedin.com/redir/invalid-link-page?url=http%3A%2F%2FSKILL%2emd)) instead of bloating the context window is a massive game-changer for both runtime efficiency and accuracy.  
Quick question: When the routing layer selects the correct skill but execution fails downstream, do you handle recovery via meta-skills or rely on standard application-level retry loops?

…more

Like

Reply

[

![View Rana Usman Ahmad’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEeoxS1XpzVRA/profile-displayphoto-scale_100_100/B4EZ78iE4JKAAY-/0/1782353255903?e=1789603200&v=beta&t=sPEj4i6i6DclLC5yCh102P1PdwdbhgC8DYPAUS_phpU)



](https://www.linkedin.com/in/rana-usman825)[

### Rana Usman Ahmad   • 3rd+

Microsoft Security Architect | Azure, Zero Trust, Purview DLP | Cybersecurity Architect Expert | UK and EU Enterprise | MCT

](https://www.linkedin.com/in/rana-usman825)

1d

The real advantage isn’t the model size, but how reliably the agent is guided through the right workflow. Strong skills, clear boundaries, and traceable tool use turn capability into dependable execution.

Like

Reply

[

![View Luccas Mota’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQExaZE-QFbf6A/profile-displayphoto-scale_100_100/B4DZh3wFhnHwAc-/0/1754355752565?e=1789603200&v=beta&t=eSrhw7DUuETu6I3JIXoRhIKdefiSfVB5jWdFbM4Hzgk)



](https://www.linkedin.com/in/luccas-mota-852b1792)[

### Luccas Mota   • 2nd

Senior AI Product Manager (remote) | 10+ years of experience | AI Product Builder | Driving 0→1 and growth at scale | GenAI

](https://www.linkedin.com/in/luccas-mota-852b1792)

1d

I also think the description field deserves more attention. It's essentially prompt engineering one layer down, and small mistakes may only become visible when you have dozens of skills competing to handle the same task.

Like

Reply

[

![View Nick Curum’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQFyxjg2SJ2l8g/profile-displayphoto-shrink_100_100/B56ZdVMgGVHEAc-/0/1749481030627?e=1789603200&v=beta&t=Oc2PwnQwQNsPPI7rfqeTxT9u9eUrK8kbhngRlE5ukP8)



](https://www.linkedin.com/in/nick-curum)[

### Nick Curum   • 2nd

I help professionals build property portfolios with boardroom discipline • Building a seven-figure portfolio alongside the day job • First Output, weekly on capital allocation

](https://www.linkedin.com/in/nick-curum)

1d

The necessity of clear skill descriptions and testing underlines how practical design shapes AI agent effectiveness. Bigger models alone can’t fill the gaps in process clarity.

Like

Reply

[

![View Patrick E Calderon’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQHsgMhgoQHuow/profile-displayphoto-scale_100_100/B4DZ6naJfPJ0AY-/0/1780925112465?e=1789603200&v=beta&t=QFgfi6mEpiNT8_3HVT2woG9ia82tRkMocZuudQtujK4)



](https://www.linkedin.com/in/patrickcalderondakin)[

### Patrick E Calderon   • 2nd

Founder & CEO, MEMStorage | Building the Enterprise AI Execution Gateway | AI Governance • Execution Control • Enterprise Infrastructure

](https://www.linkedin.com/in/patrickcalderondakin)

1d

“Make bad actions impossible in software” is the key. Once agents can act, enforcement cannot depend entirely on the model choosing the right path. The execution boundary itself needs deterministic controls.  

Like

Reply

[

![View Sandeep Gulati🎯’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQHN6d5oG9YUcg/profile-displayphoto-shrink_100_100/B4EZbtFMwUGUAc-/0/1747734286904?e=1789603200&v=beta&t=2ctbDK6sS1FllmPY4xdH3W9Ks-sI_gMPS2qSww5Q3-U)



](https://www.linkedin.com/in/sangulati)[

### Sandeep Gulati🎯   • 3rd+

AI Marketing Leader | Architect of Growth-Focused, Results-Driven GTM Strategies | Driving High-Impact Media, Performance Marketing & Scalable Campaigns for World-Class Brands

](https://www.linkedin.com/in/sangulati)

1d

Models become interchangeable faster than institutional knowledge. The real advantage is embedding what your organisation knows into repeatable workflows others cannot easily copy.

Like

Reply

[

![View Mihir Jha’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQE3ldTiQkjZEQ/profile-displayphoto-shrink_100_100/B4EZTNcf4wHUAU-/0/1738613588604?e=1789603200&v=beta&t=AB_j5T0OI18jvJtNBMomd7dXZ4txwXKVHl2BRlNS5S0)



](https://www.linkedin.com/in/mihirkrjha)[

### Mihir Jha   • 3rd+

Cloud & Microservices Architect | Enterprise AI Engineer | GCP Professional Cloud Architect | Microsoft Certified: Azure Fundamentals | IBM AI Engineering Professional Certificate

](https://www.linkedin.com/in/mihirkrjha)

1d

The description field is an interesting design constraint because it effectively becomes part of the agent's routing mechanism. A vague description can cause the right skill to remain unused, while an overly broad one can create the wrong tool path.

Like

Reply

[

![View Wil Klusovsky’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQECO_bgoY29wg/profile-displayphoto-scale_100_100/B4EZ.z5wsTIkAY-/0/1785429694281?e=1789603200&v=beta&t=GNHc5DVV6Q4Kuw0J_31h2ohm4TXP__18_WXVDpX0A2k)



](https://www.linkedin.com/in/wilklu)[

### Wil Klusovsky   • 2nd

Helping Executives, Boards & Technology Leaders Reduce Cyber Risk | Business-First Cybersecurity | CRO at viLogics | Public Speaker

](https://www.linkedin.com/in/wilklu)

1d

The moat won’t be the model.  
It’ll be the operating system around it: the runbooks, guardrails, tool paths, and judgment your best people already use.

Like

Reply

[

![View Alex Miguel Meyer’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQG3agYAECoSSA/profile-displayphoto-shrink_100_100/B4EZcx7PYBHsAU-/0/1748889302974?e=1789603200&v=beta&t=RYMxunEwgW7G9a5_ZPKHeNAWhNYvgGOITWixQIOShb4)



](https://www.linkedin.com/in/alexander-miguel-meyer)[

### Alex Miguel Meyer   • 2nd

Executive AI Advisor | Keynote Speaker & Educator I Critical Thinking in the AI Age I AI Governance I Human-AI Collaboration

](https://www.linkedin.com/in/alexander-miguel-meyer)

1d

In complex systems, performance usually improves when ambiguity is removed from execution, [Sairam](https://www.linkedin.com/in/sairam-sundaresan/)! Clear boundaries often matter more than adding capability.

Like

Reply

[

![View Jose Luis Flores® ☁’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQFH0Gnp_9iQOQ/profile-displayphoto-scale_100_100/B56Zv99k96HIAc-/0/1769492336999?e=1789603200&v=beta&t=tpAXh3G0U_diAs3SkXakOgWX3N7i1Dw3UOaHEIczHEg)



](https://www.linkedin.com/in/joseluisfloresflores)[

### Jose Luis Flores® ☁   • 3rd+

AI Governance Architect | Enterprise AI Risk & Compliance (NIST AI RMF, ISO/IEC 42001) | Microsoft 365, Entra ID & Cloud Security | 20+ Yrs Federal & Fortune 500 | Responsible AI Adoption | Bilingual EN/ES

](https://www.linkedin.com/in/joseluisfloresflores)

21h

The boundaries line is the one I would underline because most teams check the answer and never once look at which tools the agent touched to get there.

Like

Reply

[

![View Thiago Salvador’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQFA-ku0cZejZQ/profile-displayphoto-scale_100_100/B4DZ2WpAtoIkAc-/0/1776348831343?e=1789603200&v=beta&t=VaMU17xcyL63aDDX428CElEi-8AVRD-NC-4UUQtBnr0)



](https://www.linkedin.com/in/salvadorthiago)[

### Thiago Salvador   • 3rd+

AI & Operations Leader | Driving Business Connecting Humans and Machines

](https://www.linkedin.com/in/salvadorthiago)

23h

i'd take the token bill over an agent working from a partial picture. one that's missing a reference rarely stops to ask, it just answers anyway.

Like

Reply

[

![View Francisco Martinez’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQF1jfTBJR6uGw/profile-displayphoto-scale_100_100/B4EZ6e7CYKIoAg-/0/1780782738977?e=1789603200&v=beta&t=j2WTxr0QqgLhZqfTLtiX8cqJXCbWUhsVlBl_sKC8Ob4)



](https://www.linkedin.com/in/franciscoamartinez2016)[

### Francisco Martinez   • 3rd+

Founder & Writer developing & deploying sales leaders. I write for ambitious people who lead without a title and choose to be indispensable.

](https://www.linkedin.com/in/franciscoamartinez2016)

1d

The model may be accessible to everyone, but the way your best people actually work is much harder to replicate, [Sairam](https://www.linkedin.com/in/sairam-sundaresan/).

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Francisco Martinez’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Francisco Martinez](https://www.linkedin.com/in/franciscoamartinez2016/) The model is increasingly becoming the commodity. The real advantage is capturing the context, judgment, workflows, and decision-making that make a strong team effective.

Like

Reply

[

![View Jeremiah Teo’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQGtQ5j5oXu9bA/profile-displayphoto-scale_100_100/B56ZfeVtuZG0Ac-/0/1751781928211?e=1789603200&v=beta&t=HiH3m9iq7CcqQ4aat6NXAa1J9NfO_d6tSf4uFzZYpWc)



](https://www.linkedin.com/in/jeremiah-teo-charisma-business-coach)[

### Jeremiah Teo   • 3rd+

The Charisma Business Coach (No.1 Career Coach 🇭🇰) ​> 100 Millions’ Views & ​Engagements 📈 Championed 5k+ C-Suite Leaders towards 10-1,000x Brand Transformation in 8 Weeks 🚀 Top 1% LinkedIn 🏆 University Lecturer 🎤

](https://www.linkedin.com/in/jeremiah-teo-charisma-business-coach)

1d

This is a great way to frame the real advantage with AI agents. The model may be shared, but the workflows, judgment, and institutional knowledge built around it are much harder to replicate. [Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/)

Like

Reply

[

![View Cynthia Chan’s  graphic](https://media.licdn.com/dms/image/v2/C5603AQEhSi_D-Isr1A/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1634331222638?e=1789603200&v=beta&t=bqIe3UYZM0CuJM0GXrvllLBjdLfYAGAzg4L23pTQ4r4)



](https://www.linkedin.com/in/cynthiaychan)[

### Cynthia Chan   • 3rd+

Leadership Coach | Business Strategist | Psychotherapist | Helping High Achievers Align Identity & Leadership

](https://www.linkedin.com/in/cynthiaychan)

1d

Specialized skills reduce noise around complex tasks. Context should arrive when work requires it. That keeps agents focused without losing flexibility.

Like

Reply

[

![View Ashley Nicholson’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQH2FMnxh8uFVQ/profile-displayphoto-scale_100_100/B4EZw_Du_RGoAc-/0/1770584470844?e=1789603200&v=beta&t=L3IBRzuCDCv0GPEG-PGeZfrx6wT4C50UkDQQ38UQr2Y)



](https://www.linkedin.com/in/ashley--nicholson)[

### Ashley Nicholson   • 3rd+

Turning Data Into Better Decisions | Follow Me for More Tech Insights | Technology Leader & Entrepreneur

](https://www.linkedin.com/in/ashley--nicholson)

1d

This is a big shift. Better AI may not come from bigger models, but from better ways of telling them how work should get done. The skill library could become a real advantage.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Ashley Nicholson’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Ashley Nicholson](https://www.linkedin.com/in/ashley--nicholson/) And that advantage should compound over time. A well maintained skill library can turn lessons from repeated work into reusable system behavior.  

Like

Reply

[

![View Leslie Babel’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQECHAyhXcWWzg/profile-displayphoto-scale_100_100/B56Zvh4fk7KIAc-/0/1769021242954?e=1789603200&v=beta&t=UU-5g8kEDLD_W4P49iKC3FjJ7Pqa01m76cdFvznAZgg)



](https://www.linkedin.com/in/lesliebabel)[

### Leslie Babel   • 3rd+

The Tech Simplifier Officer | Managed IT + Cybersecurity + AI | Coach to SMBs | CEO, Digital Fire | Follow for posts about breaking down complex tech, building better systems, and helping you succeed :)

](https://www.linkedin.com/in/lesliebabel)

1d

Workflow knowledge becomes the real moat when models and tools are equally accessible.

Like

Reply

[

![View Abdul Rehman’s  graphic](https://media.licdn.com/dms/image/v2/D4D03AQEEZIthc-fKxA/profile-displayphoto-scale_100_100/B4DZ6cC3x2KUAY-/0/1780734460269?e=1789603200&v=beta&t=iBazfoJseKCULrH7w7M6qHjuTy-xTxUQFExFpSUPmlM)



](https://www.linkedin.com/in/arehman29)[

### Abdul Rehman   • 3rd+

Helping SaaS | Tech | Ai Platforms To Turn Their Complex Products Into Clear Stories

](https://www.linkedin.com/in/arehman29)

1d

[Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/) Great leaders understand that logic may explain the decision, but empathy and emotional awareness determine whether people can actually get behind it.

Like

Reply

[

![View Patrick Giwa, PhD’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEtLbgbCpfw5A/profile-displayphoto-scale_100_100/B4EZhDwLutHgAc-/0/1753483362928?e=1789603200&v=beta&t=f5tDPuT7CjuoS4R8GC21gLBcB9oqUhMkMIEfvK-mnl8)



](https://www.linkedin.com/in/patrickgiwa)[

### Patrick Giwa, PhD   • 2nd

I train and deploy AI agents for small businesses (DM for how) | Follow for posts on AI, Product Management and SMB business growth

](https://www.linkedin.com/in/patrickgiwa)

1d

Really like the shift from bigger models to better workflows. AI becomes much more useful when it understands the process behind the work, not just the information. [Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/)

Like

Reply

[

![View Pooja Jain’s open to work graphic](https://media.licdn.com/dms/image/v2/D4D35AQGGMLttRk3Upg/profile-framedphoto-shrink_100_100/B4DZ.k4l.2IwAc-/0/1785177727492?e=1788433200&v=beta&t=-De_Lks34Mz833ElGCngH00EyPwkdg-PW1LaS2ny1i0)



](https://www.linkedin.com/in/pooja-jain-898253106)[

### Pooja Jain   • 2nd

Storyteller | Data Architect | Building Scalable Data & AI Foundations for Enterprise Performance | Linkedin Top Voice 2025,2024 | Open to collaboration

](https://www.linkedin.com/in/pooja-jain-898253106)

1d

Amazing read and thoughtful share by Google! I like the focus on, that point on testing for how the agent got there rather than just the final answer touches on the most critical challenge in autonomous agent evaluation!!! [Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/)

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)4

Reply1 reply1 Comment on Pooja Jain’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Pooja Jain](https://www.linkedin.com/in/pooja-jain-898253106/) The final answer can look correct while the path taken to reach it is fragile. Evaluating the trajectory gives us a much better view of whether an autonomous agent can actually be trusted.

Like

Reply

[

![View Harit Bhasin’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQGJHx4SSlweAg/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1710690133931?e=1789603200&v=beta&t=iLy6PPI5wOVz_66U4xWel_NGIfuB0UazOrICQxC9No4)



](https://www.linkedin.com/in/bhasinharit948)[

### Harit Bhasin   • 3rd+

Leadership & Career Coach • Product Development Leader • Helping tech leaders get promoted with influence & presence • Follow for leadership & career growth tips

](https://www.linkedin.com/in/bhasinharit948)

1d

Definitely, bigger models cannot solve workflows that lack clear instructions and strong boundaries.  
  
Well designed skills turn team knowledge into repeatable actions, making agents more reliable and useful. [Sairam](https://www.linkedin.com/in/sairam-sundaresan/)

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Harit Bhasin’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Harit Bhasin](https://www.linkedin.com/in/bhasinharit948/) Skills turn general capability into repeatable behaviour, which is what makes an agent useful beyond a one-off demonstration.

Like

Reply

[

![View Dipin Kanojia’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQGU-Rgoxntp7A/profile-displayphoto-scale_100_100/B56Z7MCrcoG0AY-/0/1781539718744?e=1789603200&v=beta&t=bUPCkkh2_1NwvksXmSpdkdPoRceaJRV-ac8r1XpZA5U)



](https://www.linkedin.com/in/dipin-kanojia)[

### Dipin Kanojia   • 3rd+

Turning AI Pilots Into Production Reality | Fortune 500 AI Project Lead | Sharing AI, AI Agents & Enterprise Adoption Insights | AI Certified | 200K+ Impressions

](https://www.linkedin.com/in/dipin-kanojia)

1d

[Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/) Loading only the skill you need instead of everything at once makes total sense for keeping agents focused and accurate.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply

[

![View Hina Arora’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQHuvefLLLDhug/profile-displayphoto-shrink_100_100/B56ZRLarEaGsAY-/0/1736432072363?e=1789603200&v=beta&t=MZEe6716i9M74Kw9nNgoX3_XmSqb8q_7Ri5VZu4np80)



](https://www.linkedin.com/in/careerwithhina)[

### Hina Arora   • 3rd+

Helping CTOs, EMs & Tech Founders Build Industry Authority Through AI-Led Thought Leadership | Founder @BrandBuilders | Tech / AI / Career Content Creator (500K+) | 10+ YEO in Tech & AI

](https://www.linkedin.com/in/careerwithhina)

1d

A strong reminder that better context selection can matter more than simply adding more context [Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/).

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Hina Arora’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Hina Arora](https://www.linkedin.com/in/careerwithhina/) More context can add noise if the system cannot identify what matters for the task. Good context selection is an engineering problem in its own right.

Like

Reply

[

![View Raul Junco’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQElWXg4JIEOMw/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1669834773963?e=1789603200&v=beta&t=TLLlq9WBmpjV9rK-VK2CEeHpr1O93_-CpLqkmlXw7VA)



](https://www.linkedin.com/in/raul-junco)[

### Raul Junco   • 2nd

Simplifying System Design

](https://www.linkedin.com/in/raul-junco)

(edited)1d

A bad runbook loaded at the right moment is still a bad runbook; same with skills

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Raul Junco’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Raul Junco](https://www.linkedin.com/in/raul-junco/) A skill is only useful if its instructions are sound and its trigger conditions are clear. Good selection cannot compensate for flawed underlying logic.  

Like

Reply

[

![View Leon Jose’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQH791ZHFro7RQ/profile-displayphoto-scale_100_100/B56Z78zwqgKgAY-/0/1782357891243?e=1789603200&v=beta&t=dG49q_btzt1rjBPwKySDhiW5in_cDa5NB3RtId12qmo)



](https://www.linkedin.com/in/ileonjose)[

### Leon Jose   • 3rd+

I automate the ops work your team keeps putting off | AI Consultation

](https://www.linkedin.com/in/ileonjose)

1d

Spot on! Giving AI better instructions is way more useful than just making the model bigger.

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply1 reply1 Comment on Leon Jose’s comment

[

![View Sairam Sundaresan’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEexBpZqzn8wA/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1702676427081?e=1789603200&v=beta&t=hZyT6fprJBLRien7EpuaXcb-YULDvDG5xZyJxXlXE74)



](https://www.linkedin.com/in/sairam-sundaresan)[

### Sairam Sundaresan Author

AI Engineering Leader | Author of AI for the Rest of Us | I help engineers land AI roles and companies build valuable products

](https://www.linkedin.com/in/sairam-sundaresan)

1d

[Leon Jose](https://www.linkedin.com/in/ileonjose/) Yes. Bigger models can improve capability, but better instructions and workflows often determine whether that capability translates into reliable results.  

Like

Reply

[

![View Luna V.’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQGle1C3jpq18A/profile-displayphoto-scale_100_100/B4EZ_OC.hhIAAY-/0/1785868315559?e=1789603200&v=beta&t=eCyd9K4riqppkxwYuIojv-pzMypMp_R5AWAm7Uo4Vto)



](https://www.linkedin.com/in/lunavega)[

### Luna V.   • 3rd+

Build an AI-Automated Online Income from Day One, No Massive Audience needed. Skip My 10 Years of Learning This the Hard Way.

](https://www.linkedin.com/in/lunavega)

1d

Models and tools are becoming increasingly accessible, so the real advantage starts moving into the layer of how a company actually works.

Like

Reply

[

![View Guilherme Martins’  graphic](https://media.licdn.com/dms/image/v2/D4D03AQG8ogEppinAlw/profile-displayphoto-scale_100_100/B4DZyAo5YrKQAc-/0/1771684731130?e=1789603200&v=beta&t=V2_HIXiUU6R682SU6OtAdwM0LJWFLtYvV7je-WVFdkk)



](https://www.linkedin.com/in/gmartins-dev)[

### Guilherme Martins   • 2nd

Software Engineer | Full-Stack Developer | Software Architecture | AI-Driven Engineering

](https://www.linkedin.com/in/gmartins-dev)

1d

[Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/) Hi!  
I’m building sdd-agentic-flow, an open-source, local-first harness for AI coding agents: [https://www.linkedin.com/posts/gmartins-dev_ai-generativeai-aiagents-share-7494755186167660545-kJQ1](https://www.linkedin.com/posts/gmartins-dev_ai-generativeai-aiagents-share-7494755186167660545-kJQ1)  
I’d love for you to check it out. Any feedback or sharing would be greatly appreciated!

…more

[

![](https://media.licdn.com/dms/image/sync/v2/D4D27AQHkCy2ndBxg8w/articleshare-shrink_160/B4DaARtcErKwAQ-/0/1787003519862?e=1788433200&v=beta&t=nr8pyBARN2b3cf22IjMMXx_W0k-fflCNbSdRblLtcuw)



](https://www.linkedin.com/feed/update/urn:li:activity:7494755187111325696)[

## #ai #generativeai #aiagents #codingagents #aiengineering #softwareengineering #developertools #opensource #developerexperience #sdd #specificationdrivendevelopment #agenticengineering #ia… | Guilherme Martins

### Você já usa coding agents. O que falta não é mais um agente autônomo. Falta um workflow que ligue spec, execução, evidência e revisão. O sdd-agentic-flow é um harness spec-driven, local-first e open source, para workflows guiados por humanos. Instala...



](https://www.linkedin.com/feed/update/urn:li:activity:7494755187111325696)

Like

![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)1

Reply

[

![View Anas Riad’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQGg3etCOrgiAg/profile-displayphoto-shrink_100_100/B4EZYkBj0mHUAc-/0/1744361111607?e=1789603200&v=beta&t=-dyBOiTu6ALEBqHKO0ZyGdJSTFpjBWFsCW7KQRICp5s)



](https://www.linkedin.com/in/riadanas)[

### Anas Riad   • 3rd+

AI Consultant & AI Engineer | AI agents and automations built as real systems, not demos | Ex Data Scientist, 4 yrs ML | Top Rated Plus on Upwork, $90K+ earned | YouTube: Anas Riad

](https://www.linkedin.com/in/riadanas)

1d

The point about loading specialist skills only when needed is important. Too much context can make an agent worse, not better.

Like

Reply

[

![View Jennelle McGrath 😎’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQFT19mO23DEcA/profile-displayphoto-scale_100_100/B4EZ5Qtm.oJkAY-/0/1779470596545?e=1789603200&v=beta&t=k1QzklaqcaArdvg2Xjsy5mkA4mKDqK6uPlAgADi5n6Q)



](https://www.linkedin.com/in/jennellemcgrath)[

### Jennelle McGrath 😎   • 3rd+

✌️CEO at MarketVeep.com | HubSpot Marketing Agency | PMA Board | Speaker | 2 x INC 5000 | HubSpot Diamond Partner | Be Kind 🫶

](https://www.linkedin.com/in/jennellemcgrath)

1d

[Sairam Sundaresan](https://www.linkedin.com/in/sairam-sundaresan/) Focusing on well-defined runbooks and specialist skills helps agents handle complex workflows with incredible precision!

Like

Reply

[

![View Jonathan Maharaj FCPA’s  graphic](https://media.licdn.com/dms/image/v2/D5603AQEg1MHruN-bdA/profile-displayphoto-scale_100_100/B56ZwM4tROHQAc-/0/1769742721599?e=1789603200&v=beta&t=biowZOPESBFtbEXB4tUqCU0oloBEOt2WqqkGs5ILqpM)



](https://www.linkedin.com/in/jonathanmaharaj)[

### Jonathan Maharaj FCPA   • 2nd

Founder | Harvard Masters Student | Financial Wisdom for Life, Business & Leadership | Helping people think better about money, decisions & the future

](https://www.linkedin.com/in/jonathanmaharaj)

1d

Descriptions are crucial to help agents choose the right skills.

Like

Reply

[

![View Tariq Sheikh’s  graphic](https://media.licdn.com/dms/image/v2/D4E03AQEV9wjvONKLwA/profile-displayphoto-scale_100_100/B4EZ8nJfctJMAY-/0/1783068229672?e=1789603200&v=beta&t=ai3BwEPxREe0X8E6QnkOpHvPvkL_okCglBCw3znZF4A)



](https://www.linkedin.com/in/tariq-sheikh-agent-for-lawyers)[

### Tariq Sheikh   • 3rd+

The Agent for BigLaw Partners | Representation for Rainmakers + Teams billing $5M-$100M | The old way: a recruiter calls you about a job. The new way: an agent calls firms about you.

](https://www.linkedin.com/in/tariq-sheikh-agent-for-lawyers)

1d

Skills cutting context that much is impressive.

Like

Reply
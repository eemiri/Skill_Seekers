# Basecamp-Shapeup - Other

**Pages:** 26

---

## Acknowledgements | Shape Up

**URL:** https://basecamp.com/shapeup/0.2-acknowledgements

**Contents:**
- Acknowledgements
- Shape Up
- Preface
  - Foreword by Jason Fried
  - Acknowledgements
  - Introduction
- Part 1: Shaping
  - Principles of Shaping
  - Set Boundaries
  - Find the Elements

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Jason Fried and David Heinemeier Hansson, Basecamp’s founders, planted many of the seeds for this book. It is informed by their values, Basecamp’s culture, and fifteen years of collaborative trial-and-error.

Bob Moesta and Chris Spiek made pivotal contributions. This book wouldn’t have come together without their help.

Yaneer Bar-Yam’s lectures at the New England Complex Systems Institute helped me structure the method.

The expert designers and programmers at Basecamp tried, tested, and improved these techniques over the years to ship real projects. Their efforts make this a book of practice, not theory.

Copyright ©1999-2025 37signals LLC. All rights reserved.

Stop Running in Circles and Ship Work that Matters

Buy the print edition

---

## Foreword by Jason Fried | Shape Up

**URL:** https://basecamp.com/shapeup/0.1-foreword

**Contents:**
- Foreword by Jason Fried
- Shape Up
- Preface
  - Foreword by Jason Fried
  - Acknowledgements
  - Introduction
- Part 1: Shaping
  - Principles of Shaping
  - Set Boundaries
  - Find the Elements

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Acknowledgements

The way a team works has an enormous influence on what it can do. The process, the methods, the practices, the approach, the discipline, the trust, the communication style, the pace. The way—the how—is foundational and fundamental.

You’ll often hear people say “execution is everything,” but that’s not quite right. In fact, it’s often quite wrong.

When it comes to project work, and specifically software development, executing something the wrong way can destroy morale, grind teams down, erode trust, crunch gears, and wreck the machinery of long-term progress. So yeah, it’s “done,” but at what cost? By doing, what have we done to ourselves? Do we really have to do that again, over and over month after month, year after year?

How many projects have you been a part of that you’d want to do over? How many projects have gone long, piled up at the end, and burned people out? How many projects were essentially collections of unreasonable expectations? How many projects turned teams against each other, frustrated everyone from builder to stakeholder, and ultimately would have been better off dying than delivering?

Sometimes execution is everything—everything that’s wrong. So what does executing right look like?

Over the last few years, there’s been a heightened curiosity about how we work at Basecamp. People often ask us how we get so much done so quickly at such a high level of quality with such a small team. And how we keep our teams together for years and years.

For one, we’re not into waterfall or agile or scrum. For two, we don’t line walls with Post-it notes. For three, we don’t do daily stand ups, design sprints, development sprints, or anything remotely tied to a metaphor that includes being tired and worn out at the end. No backlogs, no Kanban, no velocity tracking, none of that.

We have an entirely different approach. One developed in isolation over nearly 15 years of constant trial and error, taking note, iterating, honing in, and polishing up. We’ve shaped our own way.

Blog posts, workshops, and occasional conference talks have provided glimpses of our own unique process, but we’ve never laid it bare for all to see. This book does just that.

Now that our process is fully formed, documented, and ready to go, we’re here to share it with all those curious enough to listen to a new way of doin

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#case-study-clients-in-projects

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#affordances-before-pixel-perfect-screens

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#programmers-dont-need-to-wait

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#program-just-enough-for-the-next-step

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#integrate-one-slice

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Get One Piece Done | Shape Up

**URL:** https://basecamp.com/shapeup/3.2-chapter-11#start-in-the-middle

**Contents:**
- Get One Piece Done
- Integrate one slice
- Case study: Clients in projects
- Programmers don’t need to wait
- Affordances before pixel-perfect screens
- Program just enough for the next step
- Start in the middle
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

As the team gets oriented, they start to discover and track the tasks they need to do to build the project. It’s important at this early phase that they don’t create a master plan of parts that should come together in the 11th hour. If the team completes a lot of tasks but there’s no “one thing” to click on and try out, it’s hard to feel progress. A team can do a lot of work but feel insecure because they don’t have anything real to show for it yet. Lots of things are done but nothing is really done.

Instead they should aim to make something tangible and demoable early—in the first week or so. That requires integrating vertically on one small piece of the project instead of chipping away at the horizontal layers.

We can think of projects in two layers: front-end and back-end, design and code. While technically speaking there are more layers than this, these two are the primary integration challenge in most projects.

Suppose the project starts with a lot of design. The team could design a variety of screens and even implement them as templates or views. But until they’re wired to a backend, nothing does anything. The work remains hypothetical and speculative.

Same with the backend. A lot of tasks could be checked off, but without any UI—what can you do with it? How do you judge if the work on a specific piece of business logic is really right without interacting with it?

What we want instead is to pick off one slice of the project to integrate. Then when that’s done, the team has something tangible that they’ve proven to work (or not work and reconsider). Anyone can click through the interaction and see if the feature does what it should and if what it does is what they want.

We built a feature in Basecamp 3 that allowed service firms to invite clients to their projects and share chosen documents, messages, or to-do lists with them. The concept, defined in the pitch, had a variety of moving parts:

The team had one designer and one programmer. After they got oriented and familiar with how the existing code worked, the designer chose the visibility toggle as the best place to integrate first. This was the most central piece of UI in the project. It’s the one that would appear in demo videos and the interaction customers would use most.

The designer didn’t make a pixel-perfect mockup. Instead, he experimented with differ

*[Content truncated]*

---

## Introduction | Shape Up

**URL:** https://basecamp.com/shapeup/0.3-chapter-01#growing-pains

**Contents:**
- Introduction
- Growing pains
- Six-week cycles
- Shaping the work
- Making teams responsible
- Targeting risk
- How this book is organized
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Principles of Shaping

This book is a guide to how we do product development at Basecamp. It’s also a toolbox full of techniques that you can apply in your own way to your own process.

Whether you’re a founder, CTO, product manager, designer, or developer, you’re probably here because of some common challenges that all software companies have to face.

As software teams start to grow, some common struggles appear:

Team members feel like projects go on and on, with no end in sight.

Product managers can’t find time to think strategically about the product.

Founders ask themselves: “Why can’t we get features out the door like we used to in the early days?”

We saw these challenges first-hand at Basecamp as we grew from four people to over fifty.

Basecamp started off in 2003 as a tool we built for ourselves. At the time we were a consultancy designing websites for clients. Information would get lost in the game of telephone between the client, the designer, and the person managing the project. We wanted Basecamp to be a centralized place where all parties could see the work, discuss it, and know what to do next. It turned out lots of companies had this “information slipping through the cracks” problem. Today millions of people across all kinds of industries rely on Basecamp as their shared source of truth.

Three of us built the first version. Jason Fried, Basecamp’s founder, led the design. His co-founder, David Heinemeier Hansson, programmed it (and created the well-known web framework Ruby on Rails as a by-product). At the time I was a web designer with a focus on usability and user interfaces. I executed Jason’s design direction for key features of the app and collaborated with him to fill in details of the concept.

From the first prototypes in July 2003 to launch in February 2004, David only worked ten hours a week. We knew we wouldn’t get anywhere with those ten hours of programming unless we used them very deliberately. Our intense focus on “hammering” the scope to fit within a given time budget was born under these constraints.

As the business grew, I started widening my skills. Working with David and Ruby on Rails made the world of programming accessible to me. I learned the techniques programmers use to tame complexity: things like factoring, levels of abstraction, and separation of concerns. With one foot

*[Content truncated]*

---

## Introduction | Shape Up

**URL:** https://basecamp.com/shapeup/0.3-chapter-01

**Contents:**
- Introduction
- Growing pains
- Six-week cycles
- Shaping the work
- Making teams responsible
- Targeting risk
- How this book is organized
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Principles of Shaping

This book is a guide to how we do product development at Basecamp. It’s also a toolbox full of techniques that you can apply in your own way to your own process.

Whether you’re a founder, CTO, product manager, designer, or developer, you’re probably here because of some common challenges that all software companies have to face.

As software teams start to grow, some common struggles appear:

Team members feel like projects go on and on, with no end in sight.

Product managers can’t find time to think strategically about the product.

Founders ask themselves: “Why can’t we get features out the door like we used to in the early days?”

We saw these challenges first-hand at Basecamp as we grew from four people to over fifty.

Basecamp started off in 2003 as a tool we built for ourselves. At the time we were a consultancy designing websites for clients. Information would get lost in the game of telephone between the client, the designer, and the person managing the project. We wanted Basecamp to be a centralized place where all parties could see the work, discuss it, and know what to do next. It turned out lots of companies had this “information slipping through the cracks” problem. Today millions of people across all kinds of industries rely on Basecamp as their shared source of truth.

Three of us built the first version. Jason Fried, Basecamp’s founder, led the design. His co-founder, David Heinemeier Hansson, programmed it (and created the well-known web framework Ruby on Rails as a by-product). At the time I was a web designer with a focus on usability and user interfaces. I executed Jason’s design direction for key features of the app and collaborated with him to fill in details of the concept.

From the first prototypes in July 2003 to launch in February 2004, David only worked ten hours a week. We knew we wouldn’t get anywhere with those ten hours of programming unless we used them very deliberately. Our intense focus on “hammering” the scope to fit within a given time budget was born under these constraints.

As the business grew, I started widening my skills. Working with David and Ruby on Rails made the world of programming accessible to me. I learned the techniques programmers use to tame complexity: things like factoring, levels of abstraction, and separation of concerns. With one foot

*[Content truncated]*

---

## Introduction | Shape Up

**URL:** https://basecamp.com/shapeup/0.3-chapter-01#how-this-book-is-organized

**Contents:**
- Introduction
- Growing pains
- Six-week cycles
- Shaping the work
- Making teams responsible
- Targeting risk
- How this book is organized
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Principles of Shaping

This book is a guide to how we do product development at Basecamp. It’s also a toolbox full of techniques that you can apply in your own way to your own process.

Whether you’re a founder, CTO, product manager, designer, or developer, you’re probably here because of some common challenges that all software companies have to face.

As software teams start to grow, some common struggles appear:

Team members feel like projects go on and on, with no end in sight.

Product managers can’t find time to think strategically about the product.

Founders ask themselves: “Why can’t we get features out the door like we used to in the early days?”

We saw these challenges first-hand at Basecamp as we grew from four people to over fifty.

Basecamp started off in 2003 as a tool we built for ourselves. At the time we were a consultancy designing websites for clients. Information would get lost in the game of telephone between the client, the designer, and the person managing the project. We wanted Basecamp to be a centralized place where all parties could see the work, discuss it, and know what to do next. It turned out lots of companies had this “information slipping through the cracks” problem. Today millions of people across all kinds of industries rely on Basecamp as their shared source of truth.

Three of us built the first version. Jason Fried, Basecamp’s founder, led the design. His co-founder, David Heinemeier Hansson, programmed it (and created the well-known web framework Ruby on Rails as a by-product). At the time I was a web designer with a focus on usability and user interfaces. I executed Jason’s design direction for key features of the app and collaborated with him to fill in details of the concept.

From the first prototypes in July 2003 to launch in February 2004, David only worked ten hours a week. We knew we wouldn’t get anywhere with those ten hours of programming unless we used them very deliberately. Our intense focus on “hammering” the scope to fit within a given time budget was born under these constraints.

As the business grew, I started widening my skills. Working with David and Ruby on Rails made the world of programming accessible to me. I learned the techniques programmers use to tame complexity: things like factoring, levels of abstraction, and separation of concerns. With one foot

*[Content truncated]*

---

## Introduction | Shape Up

**URL:** https://basecamp.com/shapeup/0.3-chapter-01#making-teams-responsible

**Contents:**
- Introduction
- Growing pains
- Six-week cycles
- Shaping the work
- Making teams responsible
- Targeting risk
- How this book is organized
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Principles of Shaping

This book is a guide to how we do product development at Basecamp. It’s also a toolbox full of techniques that you can apply in your own way to your own process.

Whether you’re a founder, CTO, product manager, designer, or developer, you’re probably here because of some common challenges that all software companies have to face.

As software teams start to grow, some common struggles appear:

Team members feel like projects go on and on, with no end in sight.

Product managers can’t find time to think strategically about the product.

Founders ask themselves: “Why can’t we get features out the door like we used to in the early days?”

We saw these challenges first-hand at Basecamp as we grew from four people to over fifty.

Basecamp started off in 2003 as a tool we built for ourselves. At the time we were a consultancy designing websites for clients. Information would get lost in the game of telephone between the client, the designer, and the person managing the project. We wanted Basecamp to be a centralized place where all parties could see the work, discuss it, and know what to do next. It turned out lots of companies had this “information slipping through the cracks” problem. Today millions of people across all kinds of industries rely on Basecamp as their shared source of truth.

Three of us built the first version. Jason Fried, Basecamp’s founder, led the design. His co-founder, David Heinemeier Hansson, programmed it (and created the well-known web framework Ruby on Rails as a by-product). At the time I was a web designer with a focus on usability and user interfaces. I executed Jason’s design direction for key features of the app and collaborated with him to fill in details of the concept.

From the first prototypes in July 2003 to launch in February 2004, David only worked ten hours a week. We knew we wouldn’t get anywhere with those ten hours of programming unless we used them very deliberately. Our intense focus on “hammering” the scope to fit within a given time budget was born under these constraints.

As the business grew, I started widening my skills. Working with David and Ruby on Rails made the world of programming accessible to me. I learned the techniques programmers use to tame complexity: things like factoring, levels of abstraction, and separation of concerns. With one foot

*[Content truncated]*

---

## Introduction | Shape Up

**URL:** https://basecamp.com/shapeup/0.3-chapter-01#targeting-risk

**Contents:**
- Introduction
- Growing pains
- Six-week cycles
- Shaping the work
- Making teams responsible
- Targeting risk
- How this book is organized
- Shape Up
- Preface
  - Foreword by Jason Fried

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Principles of Shaping

This book is a guide to how we do product development at Basecamp. It’s also a toolbox full of techniques that you can apply in your own way to your own process.

Whether you’re a founder, CTO, product manager, designer, or developer, you’re probably here because of some common challenges that all software companies have to face.

As software teams start to grow, some common struggles appear:

Team members feel like projects go on and on, with no end in sight.

Product managers can’t find time to think strategically about the product.

Founders ask themselves: “Why can’t we get features out the door like we used to in the early days?”

We saw these challenges first-hand at Basecamp as we grew from four people to over fifty.

Basecamp started off in 2003 as a tool we built for ourselves. At the time we were a consultancy designing websites for clients. Information would get lost in the game of telephone between the client, the designer, and the person managing the project. We wanted Basecamp to be a centralized place where all parties could see the work, discuss it, and know what to do next. It turned out lots of companies had this “information slipping through the cracks” problem. Today millions of people across all kinds of industries rely on Basecamp as their shared source of truth.

Three of us built the first version. Jason Fried, Basecamp’s founder, led the design. His co-founder, David Heinemeier Hansson, programmed it (and created the well-known web framework Ruby on Rails as a by-product). At the time I was a web designer with a focus on usability and user interfaces. I executed Jason’s design direction for key features of the app and collaborated with him to fill in details of the concept.

From the first prototypes in July 2003 to launch in February 2004, David only worked ten hours a week. We knew we wouldn’t get anywhere with those ten hours of programming unless we used them very deliberately. Our intense focus on “hammering” the scope to fit within a given time budget was born under these constraints.

As the business grew, I started widening my skills. Working with David and Ruby on Rails made the world of programming accessible to me. I learned the techniques programmers use to tame complexity: things like factoring, levels of abstraction, and separation of concerns. With one foot

*[Content truncated]*

---

## Shape Up: Stop Running in Circles and Ship Work that Matters

**URL:** https://basecamp.com/shapeup

**Contents:**
- Shape Up
- Introduction
  - Foreword by Jason Fried
  - Acknowledgements
  - Introduction
- Part 1: Shaping
  - Principles of Shaping
  - Set Boundaries
  - Find the Elements
  - Risks and Rabbit Holes

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Stop Running in Circles and Ship Work that Matters by Ryan Singer Buy the print edition Start reading → Introduction Foreword by Jason Fried Acknowledgements Chapter 1 Introduction Growing pains Six-week cycles Shaping the work Making teams responsible Targeting risk How this book is organized Part 1: Shaping Chapter 2 Principles of Shaping Wireframes are too concrete Words are too abstract Case study: The Dot Grid Calendar Property 1: It’s rough Property 2: It’s solved Property 3: It’s bounded Who shapes Two tracks Steps to shaping Chapter 3 Set Boundaries Setting the appetite Fixed time, variable scope "Good" is relative Responding to raw ideas Narrow down the problem Case study: Defining "calendar" Watch out for grab-bags Boundaries in place Chapter 4 Find the Elements Move at the right speed Breadboarding Fat marker sketches Elements are the output Room for designers Not deliverable yet No conveyor belt Chapter 5 Risks and Rabbit Holes Different categories of risk Look for rabbit holes Case study: Patching a hole Declare out of bounds Cut back Present to technical experts De-risked and ready to write up Chapter 6 Write the Pitch Ingredient 1. Problem Ingredient 2. Appetite Ingredient 3. Solution Help them see it Embedded sketches Annotated fat marker sketches Ingredient 4. Rabbit Holes Ingredient 5. No Gos Examples Ready to present How we do it in Basecamp Part 2: Betting Chapter 7 Bets, Not Backlogs No backlogs A few potential bets Decentralized lists Important ideas come back Chapter 8 The Betting Table Six-week cycles Cool-down Team and project size The betting table The meaning of a bet Uninterrupted time The circuit breaker What about bugs? Keep the slate clean Chapter 9 Place Your Bets Look where you are Existing products New products R&D mode Production mode Cleanup mode Examples Questions to ask Does the problem matter? Is the appetite right? Is the solution attractive? Is this the right time? Are the right people available? Post the kick-off message Part 3: Building Chapter 10 Hand Over Responsibility Assign projects, not tasks Done means deployed Getting oriented Imagined vs discovered tasks Chapter 11 Get One Piece Done Integrate one slice Case study: Clients in projects Programmers don’t need to wait Affordances before pixel-perfect screens Program just enough for the next step Start in the middle Chapter 12 

*[Content truncated]*

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#ingredient-1-problem

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#examples

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#ready-to-present

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#how-we-do-it-in-basecamp

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#embedded-sketches

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#ingredient-4-rabbit-holes

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#help-them-see-it

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#ingredient-3-solution

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#annotated-fat-marker-sketches

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06#ingredient-5-no-gos

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

## Write the Pitch | Shape Up

**URL:** https://basecamp.com/shapeup/1.5-chapter-06

**Contents:**
- Write the Pitch
- Ingredient 1. Problem
- Ingredient 2. Appetite
- Ingredient 3. Solution
- Help them see it
  - Embedded sketches
  - Annotated fat marker sketches
- Ingredient 4. Rabbit holes
- Ingredient 5. No Gos
- Examples

Heads up! This page uses features your browser doesn’t support. Try a modern browser like Firefox or Chrome for the best experience.

Next: Bets, Not Backlogs

We’ve got the elements of a solution now, and we’ve de-risked our concept to the point that we’re confident it’s a good option to give a team. But the concept is still in our heads or in some hard-to-decipher drawings on the whiteboard or our notebook. Now we need to put the concept into a form that other people will be able to understand, digest, and respond to.

This is where we say “Okay, this is ready to write up as a pitch.” In this chapter, we’ll walk through the ingredients of a pitch and show some fully worked out examples from real projects at Basecamp.

The purpose of the pitch is to present a good potential bet. It’s basically a presentation. The ingredients are all the things that we need to both capture the work done so far and present it in a form that will enable the people who schedule projects to make an informed bet.

There are five ingredients that we always want to include in a pitch:

It’s critical to always present both a problem and a solution together. It sounds like an obvious point but it’s surprising how often teams, our own included, jump to a solution with the assumption that it’s obvious why it’s a good idea to build this thing.

Diving straight into “what to build”—the solution—is dangerous. You don’t establish any basis for discussing whether this solution is good or bad without a problem. “Add tabs to the iPad app” might be attractive to UI designers, but what’s to prevent the discussion from devolving into a long debate about different UI approaches? Without a specific problem, there’s no test of fitness to judge whether one solution is better than the other.

Establishing the problem also lets us have a clearer conversation later when it’s time to pitch the idea or bet on it. The solution might be perfect, but what if the problem only happens to customers who are known to be a poor fit to the product? We could spend six weeks on an ingenious solution that only benefits a small percentage of customers known to have low retention. We want to be able to separate out that discussion about the demand so we don’t spend time on a good solution that doesn’t benefit the right people.

How far you have to go to spell out the problem will depend on how much context you share with the people reading the write-up. The best problem definition consists of a single specific story 

*[Content truncated]*

**Examples:**

Example 1 (plaintext):
```plaintext
small batch
```

Example 2 (plaintext):
```plaintext
betting table
```

Example 3 (plaintext):
```plaintext
Small Batch
```

Example 4 (plaintext):
```plaintext
fat marker sketch
```

---

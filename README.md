<h1 align="center">Mostafa Gamal Bisher</h1>

<p align="center">
  <strong>Accounting Manager moving into software engineering</strong><br>
  Building TypeScript and React applications with the same discipline I apply to financial controls.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/mostafagamalbisher">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white">
  </a>
  <a href="https://blog-app-mostafagamalbisher.vercel.app">
    <img alt="Live project" src="https://img.shields.io/badge/Live_project-Blog_App-000000?style=flat-square&logo=vercel&logoColor=white">
  </a>
  <img alt="Focus" src="https://img.shields.io/badge/Focus-TypeScript_%C2%B7_React_%C2%B7_Next.js-3178C6?style=flat-square">
  <img alt="Based in Saudi Arabia" src="https://img.shields.io/badge/Based_in-Saudi_Arabia-006C35?style=flat-square">
</p>

---

## The transition

I have spent more than 11 years in accounting across Saudi Arabia and Egypt, currently as an Accounting Manager. I am now building software-engineering capability deliberately, through applications I design, implement, and deploy myself.

The move is not a reset. Accounting trained me in the habits that engineering rewards: precision at data boundaries, reconciliation over assumption, controls that fail loudly instead of silently, and a working intolerance for numbers that cannot be traced to a source. Those instincts show up directly in how I build — typed domain models before UI, money stored as integers rather than floats, validation at the edges, and explicit handling of the cases that are easy to skip.

What accounting does **not** give me is engineering evidence. That has to be earned in code, which is what this profile is for.

## How I work

- **Depth before breadth.** I learn one layer properly before adding the next, rather than assembling frameworks I cannot reason about.
- **Claims tied to inspectable work.** Everything stated here points at a repository or a deployed application you can open.
- **Architecture before features.** Data boundaries, type contracts, and internationalization seams get decided early, because they are expensive to retrofit.
- **Honest scope.** In-development work is labelled as such. I would rather under-claim than have a reviewer discover the gap themselves.

## Tech stack

**Languages**

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Frameworks and libraries**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![TanStack Query](https://img.shields.io/badge/TanStack_Query-FF4154?style=flat-square&logo=reactquery&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

**Tooling**

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white)
![Prettier](https://img.shields.io/badge/Prettier-F7B93E?style=flat-square&logo=prettier&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

## Selected projects

### Blog App — deployed Next.js blog platform

A complete, deployed blog application built on the Next.js App Router with TypeScript.

- Server-side pagination and category filtering, with debounced search composed over both
- URL-driven state, so every view is shareable and back-button correct
- Typed API contracts and a `Result<T>` pattern for explicit error handling
- TanStack Query caching, responsive mobile-first layout, and system-aware dark mode

Two production deployment bugs on this project were diagnosed and fixed by me — a protection-gated `VERCEL_URL` and a stale build after a domain rename.

[**Live application**](https://blog-app-mostafagamalbisher.vercel.app) · [**Source**](https://github.com/MostafaGamalBisher/Blog-App)

### ScentHub — bilingual e-commerce foundation *(in development)*

A bilingual English/Arabic fragrance storefront, built incrementally with an emphasis on getting the domain model right before the interface.

- Locale-aware routing with runtime validation, and LTR/RTL document direction driven by the active locale
- A typed catalog and taxonomy — houses, notes, concentrations, audiences, seasons, and bottle variants — where invalid combinations fail at compile time
- Localized SAR price and number formatting via `Intl.NumberFormat`, across two scripts and two numbering systems
- Prices stored as integer halalas rather than floating-point, so currency precision is structural rather than hoped for

This is an active learning project and is deliberately labelled as incomplete: no database, authentication, cart, or checkout yet.

[**Source**](https://github.com/MostafaGamalBisher/ScentHub)

---

## GitHub activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=MostafaGamalBisher&show_icons=true&hide_border=true&theme=github_dark&hide_title=true">
    <img alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=MostafaGamalBisher&show_icons=true&hide_border=true&hide_title=true" height="150">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=MostafaGamalBisher&layout=compact&hide_border=true&theme=github_dark&langs_count=6">
    <img alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MostafaGamalBisher&layout=compact&hide_border=true&langs_count=6" height="150">
  </picture>
</p>

---

## Currently learning

Form state and schema validation (React Hook Form, Zod), client state boundaries (Zustand), and the API and persistence layer behind the storefront. Longer term: Node.js services, databases, and eventually systems-level work — in that order, and not before the layer beneath is solid.

## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-mostafagamalbisher-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafagamalbisher)

Based in Saudi Arabia (GMT+3). Open to remote frontend and full-stack opportunities.

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

We start with the `pages/index.js`. The page auto-updates as you edit the file.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

We use [Tailwind CSS](https://tailwindcss.com/) for styling. The `styles` directory contains the global styles and the `tailwind.config.js` file contains the configuration for Tailwind CSS.

The workflow for the user interface can be understood as:
- The user enters the website and is greeted with the home page.
- The user can then log into their account or create a new account.
- The user can then upload a paper (pdf) or enter the text of the abstract after which the user can search for authors, journals or articles related to the particulr abstract.
- The user can then view the results of the search and select the authors, journals or articles that they want 
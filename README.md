<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>OptimosStore • Operada por Fishtech</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <style>
    :root {
      --accent-orange: #f97316;
      --accent-orange-dark: #e67e22;
      --bg-base: #0b1120;
      --bg-card: #111827;
      --bg-input: #182032;
    }

    body {
      font-family: 'Inter', sans-serif;
      background-color: var(--bg-base);
      color: #e2e8f0;
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow-x: hidden;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    ::-webkit-scrollbar {
      width: 9px;
      height: 9px;
    }
    ::-webkit-scrollbar-track {
      background: #0f172a;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb {
      background: #475569;
      border-radius: 9999px;
      border: 2px solid #0f172a;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #f97316;
    }

    .settings-scroll {
      scrollbar-width: thin;
      scrollbar-color: #f97316 #0f172a;
    }
    .settings-scroll::-webkit-scrollbar {
      width: 9px;
    }
    .settings-scroll::-webkit-scrollbar-track {
      background: #0f172a;
      border-radius: 9999px;
    }
    .settings-scroll::-webkit-scrollbar-thumb {
      background: #f97316;
      border-radius: 9999px;
      border: 2px solid #0f172a;
    }

    input[type="date"] {
      color-scheme: dark;
    }
    input[type="date"]::-webkit-calendar-picker-indicator {
      opacity: 0;
      position: absolute;
      right: 0;
      top: 0;
      width: 2.75rem;
      height: 100%;
      cursor: pointer;
    }

    body.theme-high-contrast {
      background-color: #030712;
      color: #ffffff;
    }
    body.theme-high-contrast .bg-mosaic-overlay {
      background: radial-gradient(circle at 50% 35%, rgba(3, 7, 18, 0.72) 0%, rgba(3, 7, 18, 0.94) 72%, #030712 100%);
    }

    body.theme-light {
      background-color: #f1f5f9;
      color: #0f172a;
    }
    body.theme-light .bg-mosaic-overlay {
      background: radial-gradient(circle at 50% 35%, rgba(241, 245, 249, 0.78) 0%, rgba(226, 232, 240, 0.93) 72%, #f1f5f9 100%);
    }
    body.theme-light #logged-header {
      background-color: rgba(255, 255, 255, 0.95);
      border-color: #cbd5e1;
      color: #0f172a;
    }
    body.theme-light #logged-header .text-white {
      color: #0f172a !important;
    }
    body.theme-light #logged-header .text-slate-300,
    body.theme-light #logged-header .text-slate-200 {
      color: #334155 !important;
    }
    body.theme-light #store-view h1 span.text-white {
      color: #0f172a !important;
    }

    @keyframes modalFadeIn {
      from {
        opacity: 0;
        transform: translateY(10px) scale(0.98);
      }
      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }
    .animate-modal {
      animation: modalFadeIn 0.22s ease-out forwards;
    }

    .bg-mosaic-wrapper {
      position: fixed;
      inset: 0;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
      background-color: #0b1120;
    }

    .bg-mosaic-grid {
      position: absolute;
      top: -25%;
      left: -20%;
      width: 140%;
      height: 140%;
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 14px;
      transform: rotate(-12deg) scale(1.06);
      opacity: 0.34;
    }

    .bg-mosaic-tile {
      border-radius: 18px;
      overflow: hidden;
      background-color: #162033;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
      aspect-ratio: 4 / 3;
    }

    .bg-mosaic-tile img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .bg-mosaic-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 35%, rgba(11, 17, 32, 0.48) 0%, rgba(11, 17, 32, 0.88) 72%, #0b1120 100%);
      transition: background 0.25s ease;
    }

    .logo-condensed {
      font-family: 'Anton', 'Inter', sans-serif;
      letter-spacing: 0.01em;
    }

    @keyframes pulseGlow {
      0%, 100% { opacity: 0.45; }
      50% { opacity: 1; }
    }
    .ai-pulse {
      animation: pulseGlow 1.5s infinite ease-in-out;
    }
  </style>
</head>
<body class="antialiased selection:bg-[#f97316] selection:text-white">

  <div class="bg-mosaic-wrapper" aria-hidden="true">
    <div id="bg-mosaic-grid" class="bg-mosaic-grid"></div>
    <div class="bg-mosaic-overlay"></div>
  </div>

  <div id="toast-container" class="fixed top-4 right-4 z-[120] flex flex-col gap-2 pointer-events-none max-w-xs w-full"></div>

  <div id="side-drawer-backdrop" onclick="closeSideDrawer()" class="fixed inset-0 z-50 hidden bg-black/65 backdrop-blur-xs transition-opacity"></div>
  <aside id="side-drawer" class="fixed top-0 left-0 bottom-0 z-50 w-72 max-w-[85vw] bg-[#111827] border-r border-slate-800 shadow-2xl transform -translate-x-full transition-transform duration-200 flex flex-col justify-between p-5">
    <div class="space-y-6">
      <div class="flex items-center justify-between border-b border-slate-800 pb-4">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white shadow">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
          </div>
          <div class="leading-tight">
            <div class="font-bold text-white text-sm">OptimosStore</div>
            <div class="text-[10px] text-slate-400">Operada por Fishtech</div>
          </div>
        </div>
        <button type="button" onclick="closeSideDrawer()" aria-label="Fechar menu" class="text-slate-400 hover:text-white p-1.5 rounded-lg hover:bg-slate-800 cursor-pointer">✕</button>
      </div>

      <nav class="space-y-1.5 text-sm">
        <button
          type="button"
          onclick="closeSideDrawer(); clearSearchResults();"
          class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <span>Início / Buscador IA</span>
        </button>

        <button
          type="button"
          onclick="closeSideDrawer(); openPriceListModal();"
          class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <span class="flex items-center gap-3">
            <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span>Minha Lista de Preços</span>
          </span>
          <span id="drawer-cart-badge" class="bg-[#f97316] text-white text-[11px] font-bold px-2 py-0.5 rounded-full">0</span>
        </button>

        <button
          type="button"
          onclick="closeSideDrawer(); openAlertsModal();"
          class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <span class="flex items-center gap-3">
            <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
            <span>Meus Alertas de Oferta</span>
          </span>
          <span id="drawer-alerts-badge" class="bg-slate-800 text-orange-300 border border-orange-500/30 text-[11px] font-bold px-2 py-0.5 rounded-full">0</span>
        </button>

        <button
          type="button"
          onclick="closeSideDrawer(); openAppGuideModal();"
          class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>Informações do App & Guia</span>
        </button>

        <button
          type="button"
          onclick="closeSideDrawer(); openSettingsModal('profile');"
          class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
          </svg>
          <span>Meu Perfil</span>
        </button>

        <button
          type="button"
          onclick="closeSideDrawer(); openSettingsModal('preferences');"
          class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-200 hover:bg-[#182032] hover:text-[#f97316] font-medium transition cursor-pointer text-left"
        >
          <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span>Configurações</span>
        </button>
      </nav>
    </div>

    <div class="pt-4 border-t border-slate-800">
      <button
        type="button"
        onclick="closeSideDrawer(); logoutUser();"
        class="w-full flex items-center justify-center gap-2 bg-red-500/15 hover:bg-red-500/25 text-red-400 border border-red-500/30 font-bold text-xs py-2.5 rounded-xl transition cursor-pointer"
      >
        <span>Sair da Conta</span>
      </button>
    </div>
  </aside>

  <header id="guest-header" class="relative z-10 w-full max-w-5xl mx-auto px-4 pt-5 pb-2 grid grid-cols-2 sm:grid-cols-3 items-center gap-3">
    <div class="justify-self-start bg-[#111827]/90 backdrop-blur-md px-3.5 py-2.5 rounded-2xl shadow-lg flex items-center gap-3 border border-slate-800">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white font-extrabold text-sm tracking-tight shadow-md shadow-orange-500/20 shrink-0">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
        </svg>
      </div>
      <div class="leading-tight">
        <div class="font-bold text-white text-sm sm:text-base">OptimosStore</div>
        <div class="text-[11px] text-slate-400 font-medium">Operada por Fishtech</div>
      </div>
    </div>

    <div class="order-3 sm:order-2 col-span-2 sm:col-span-1 justify-self-center">
      <button
        type="button"
        onclick="openVisitorInfoModal()"
        title="Clique para saber mais sobre o modo Visitante"
        class="inline-flex items-center gap-2 bg-[#111827]/90 hover:bg-[#182032] active:scale-[0.98] backdrop-blur-md text-slate-200 px-4 py-2 rounded-full border border-slate-800 hover:border-[#f97316]/50 shadow-lg text-xs sm:text-sm font-semibold transition cursor-pointer"
      >
        <span class="w-2.5 h-2.5 rounded-full bg-[#f97316] animate-pulse"></span>
        <span>Visitante</span>
      </button>
    </div>

    <div class="order-2 sm:order-3 justify-self-end">
      <button
        type="button"
        id="btn-open-settings-guest"
        onclick="openSettingsModal('profile')"
        class="bg-[#111827]/90 hover:bg-[#1e293b] active:scale-[0.98] backdrop-blur-md transition text-slate-200 font-semibold text-xs sm:text-sm px-4 py-2.5 rounded-2xl shadow-lg border border-slate-800 hover:border-[#f97316]/50 flex items-center gap-2 cursor-pointer"
      >
        <svg class="w-4 h-4 text-[#f97316]" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span>Configurações</span>
      </button>
    </div>
  </header>

  <header id="logged-header" class="hidden relative z-20 w-full bg-[#121822]/95 backdrop-blur-md border-b border-slate-800/90 px-3 sm:px-6 py-2.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-2 min-w-0">
      <div class="flex items-center gap-2 sm:gap-3.5 min-w-0">
        <button
          type="button"
          onclick="openSideDrawer()"
          aria-label="Abrir menu lateral"
          class="w-9 h-9 sm:w-10 rounded-lg border border-slate-700/90 bg-[#1a202c]/80 hover:bg-slate-800 hover:border-[#f97316]/60 flex flex-col items-center justify-center gap-1.5 transition cursor-pointer shrink-0"
        >
          <span class="w-4 h-[1.5px] bg-slate-300 rounded-full"></span>
          <span class="w-4 h-[1.5px] bg-slate-300 rounded-full"></span>
          <span class="w-4 h-[1.5px] bg-slate-300 rounded-full"></span>
        </button>

        <button
          type="button"
          onclick="clearSearchResults()"
          class="flex items-center gap-2 sm:gap-2.5 text-left cursor-pointer group min-w-0"
        >
          <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white shadow-md shadow-orange-500/20 shrink-0">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
          </div>
          <div class="leading-tight min-w-0">
            <div class="font-bold text-white text-xs sm:text-sm group-hover:text-[#f97316] transition truncate">OptimosStore</div>
            <div class="text-[10px] text-slate-400 truncate">Operada por Fishtech</div>
          </div>
        </button>
      </div>

      <button
        type="button"
        onclick="openSettingsModal('profile')"
        title="Abrir Meu Perfil"
        class="flex items-center gap-1.5 sm:gap-2 text-slate-300 hover:text-white text-xs sm:text-sm font-medium px-2 sm:px-3 py-1.5 rounded-lg hover:bg-slate-800/70 transition cursor-pointer min-w-0 max-w-[130px] sm:max-w-[200px]"
      >
        <div class="w-6 h-6 rounded-full overflow-hidden bg-slate-800 border border-slate-700 flex items-center justify-center shrink-0">
          <img id="logged-header-avatar-img" src="" alt="" class="hidden w-full h-full object-cover" />
          <svg id="logged-header-avatar-icon" class="w-3.5 h-3.5 text-[#f97316] shrink-0" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
          </svg>
        </div>
        <span id="logged-header-username" class="truncate">Gustavo</span>
      </button>

      <div class="flex items-center shrink-0">
        <button
          type="button"
          onclick="openSettingsModal('profile')"
          title="Configurações"
          class="flex items-center gap-1.5 sm:gap-2 text-slate-200 hover:text-white text-xs sm:text-sm font-medium p-2 sm:px-2.5 sm:py-1.5 rounded-lg hover:bg-slate-800/70 transition cursor-pointer"
        >
          <svg class="w-4 h-4 text-[#f97316] shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span class="hidden sm:inline">Configurações</span>
        </button>
      </div>
    </div>
  </header>

  <main id="main-container" class="relative z-10 flex-1 w-full max-w-5xl mx-auto px-4 py-6 sm:py-8 flex flex-col items-center">

    <div id="auth-view" class="w-full flex flex-col items-center">

      <section class="w-full max-w-[420px] bg-[#111827]/95 backdrop-blur-md rounded-2xl shadow-2xl border border-slate-800/90 p-7 sm:p-9">
        <div class="flex flex-col items-center text-center mb-7">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white shadow-lg shadow-orange-500/30 mb-4">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2.1" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
          </div>
          <h1 class="text-2xl sm:text-[26px] font-black tracking-wide text-[#f97316] uppercase">
            OPTIMOSTORE
          </h1>
          <p class="text-xs sm:text-sm text-slate-400 mt-1 font-medium">
            Bem-vindo ao OptimosStore
          </p>
        </div>

        <form id="login-form" onsubmit="handleLoginSubmit(event)" class="space-y-4">
          <div>
            <label for="login-identifier" class="block text-xs font-semibold text-slate-300 mb-1.5">
              Usuário ou E-mail
            </label>
            <input
              type="text"
              id="login-identifier"
              name="username"
              placeholder="Seu usuário ou e-mail"
              required
              autocomplete="username"
              class="w-full bg-[#182032] text-slate-100 placeholder-slate-500 text-sm px-3.5 py-2.5 rounded-lg border border-slate-700/80 focus:border-[#f97316] focus:ring-1 focus:ring-[#f97316] outline-none transition"
            />
          </div>

          <div>
            <label for="login-password" class="block text-xs font-semibold text-slate-300 mb-1.5">
              Senha
            </label>
            <div class="relative">
              <input
                type="password"
                id="login-password"
                name="password"
                placeholder="Sua senha"
                required
                autocomplete="current-password"
                class="w-full bg-[#182032] text-slate-100 placeholder-slate-500 text-sm pl-3.5 pr-10 py-2.5 rounded-lg border border-slate-700/80 focus:border-[#f97316] focus:ring-1 focus:ring-[#f97316] outline-none transition"
              />
              <button
                type="button"
                onclick="togglePasswordField('login-password', 'eye-login')"
                aria-label="Mostrar ou ocultar senha"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-200 p-1 cursor-pointer transition"
              >
                <svg id="eye-login" class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                </svg>
              </button>
            </div>
          </div>

          <div class="flex items-center justify-between pt-0.5">
            <label for="login-remember" class="inline-flex items-center gap-2 cursor-pointer select-none">
              <input
                type="checkbox"
                id="login-remember"
                checked
                class="w-3.5 h-3.5 rounded border-slate-700 bg-[#182032] text-[#f97316] focus:ring-[#f97316] accent-[#f97316] cursor-pointer"
              />
              <span class="text-xs text-slate-400">Lembrar sessão neste dispositivo</span>
            </label>
          </div>

          <div class="pt-1">
            <button
              type="submit"
              id="btn-login-submit"
              class="w-full bg-[#e67e22] hover:bg-[#f97316] active:scale-[0.99] text-white font-bold text-sm py-3 px-4 rounded-lg shadow-lg shadow-orange-500/20 transition cursor-pointer"
            >
              Acessar o OptimosStore
            </button>
          </div>

          <div class="pt-2 text-center space-y-2 text-xs">
            <div>
              <button
                type="button"
                onclick="openRecoveryModal()"
                class="text-[#f97316] hover:text-[#fb923c] font-medium hover:underline transition cursor-pointer"
              >
                Esqueceu a senha?
              </button>
            </div>
            <div class="text-slate-400">
              <span>Você não tem conta?</span>
              <button
                type="button"
                onclick="openRegisterModal()"
                class="text-[#f97316] hover:text-[#fb923c] font-semibold hover:underline ml-1 transition cursor-pointer"
              >
                Crie uma aqui
              </button>
            </div>
          </div>
        </form>
      </section>

      <section class="w-full max-w-5xl mt-16 sm:mt-20 pt-10 border-t border-slate-800/80">
        <div class="text-center max-w-xl mx-auto mb-10">
          <h2 class="text-xl sm:text-2xl font-extrabold text-white flex items-center justify-center gap-2">
            <span>🚀</span>
            <span>Informações do App & Guia Completo</span>
          </h2>
          <p class="text-xs sm:text-sm text-[#f97316] font-medium mt-1.5">
            Tudo o que você precisa saber sobre a plataforma OptimosStore
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-5">
          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">💡</span>
                <h3 class="font-bold text-[#fb923c] text-sm">O que é o OptimosStore?</h3>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                O ecossistema definitivo de pesquisa inteligente, comparação de preços e fichas técnicas desenvolvido pela <strong class="text-white">Fishtech</strong>. Projetado para otimizar suas compras com análises de custo-benefício e ofertas verificadas.
              </p>
            </div>
          </div>

          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">🔒</span>
                <h3 class="font-bold text-[#fb923c] text-sm">Segurança e Privacidade Total</h3>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Seus dados, listas e credenciais são armazenados localmente no seu dispositivo utilizando criptografia via <strong class="text-white">LocalStorage</strong>, sem rastreamento invasivo.
              </p>
            </div>
          </div>

          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">📊</span>
                <h3 class="font-bold text-[#fb923c] text-sm">Comparação Inteligente</h3>
              </div>
              <ul class="space-y-2 text-xs text-slate-300 leading-relaxed">
                <li class="flex items-start gap-2">
                  <span class="text-[#f97316] font-bold">•</span>
                  <span><strong class="text-white">Menor Preço Real:</strong> Varredura instantânea nas principais lojas online.</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-[#f97316] font-bold">•</span>
                  <span><strong class="text-white">Ficha Técnica Oficial:</strong> Dados verificados e bulários da Anvisa.</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="text-[#f97316] font-bold">•</span>
                  <span><strong class="text-white">Índice Custo-Benefício:</strong> Cruzamento direto entre preço e qualidade.</span>
                </li>
              </ul>
            </div>
          </div>

          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">🤖</span>
                <h3 class="font-bold text-[#fb923c] text-sm">IA Auxiliadora OptimosStore</h3>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Nossa IA integrada à web responde às suas dúvidas técnicas, compara concorrentes diretos e avalia se vale a pena comprar qualquer produto na hora.
              </p>
            </div>
          </div>

          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">🏆</span>
                <h3 class="font-bold text-[#fb923c] text-sm">Alertas e Economia</h3>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Acompanhe suas metas de economia, salve itens na sua Lista de Preços pessoal e ative alertas automáticos para nunca pagar mais caro.
              </p>
            </div>
          </div>

          <div class="bg-[#0e1525]/95 border border-slate-800/90 rounded-2xl p-6 shadow-xl flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-2 mb-3">
                <span class="text-base">🔗</span>
                <h3 class="font-bold text-[#fb923c] text-sm">Links Rápidos e Termos</h3>
              </div>

              <div class="flex flex-col gap-2 pt-0.5">
                <button type="button" onclick="openInstitutionalModal('termos')" class="w-full bg-[#132038] hover:bg-[#1c2e4f] border border-[#f97316]/30 hover:border-[#f97316] text-orange-300 hover:text-white text-xs font-semibold py-2 px-3 rounded-lg transition cursor-pointer flex items-center justify-center gap-2">
                  <span>📄</span>
                  <span>Termos de Serviço</span>
                </button>
                <button type="button" onclick="openInstitutionalModal('privacidade')" class="w-full bg-[#132038] hover:bg-[#1c2e4f] border border-[#f97316]/30 hover:border-[#f97316] text-orange-300 hover:text-white text-xs font-semibold py-2 px-3 rounded-lg transition cursor-pointer flex items-center justify-center gap-2">
                  <span>🔒</span>
                  <span>Política de Privacidade</span>
                </button>
                <button type="button" onclick="openInstitutionalModal('guia')" class="w-full bg-[#132038] hover:bg-[#1c2e4f] border border-[#f97316]/30 hover:border-[#f97316] text-orange-300 hover:text-white text-xs font-semibold py-2 px-3 rounded-lg transition cursor-pointer flex items-center justify-center gap-2">
                  <span>📖</span>
                  <span>Guia do Comprador</span>
                </button>
                <button type="button" onclick="openInstitutionalModal('transparencia')" class="w-full bg-[#132038] hover:bg-[#1c2e4f] border border-[#f97316]/30 hover:border-[#f97316] text-orange-300 hover:text-white text-xs font-semibold py-2 px-3 rounded-lg transition cursor-pointer flex items-center justify-center gap-2">
                  <span>🛡️</span>
                  <span>Transparência de Ofertas</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <p class="text-center text-[11px] text-slate-500 mt-8 font-medium">
          © 2026 Fishtech. Todos os direitos reservados. OptimosStore é uma marca registrada.
        </p>
      </section>
    </div>

    <section id="store-view" class="hidden w-full flex-1 flex flex-col items-center justify-center min-h-[calc(100vh-110px)] transition-all duration-300">
      <div id="search-hero-box" class="w-full max-w-[680px] mx-auto flex flex-col items-center text-center px-1 sm:px-2 transition-all duration-300">
        <h1 id="store-hero-logo" class="logo-condensed text-5xl sm:text-7xl select-none tracking-tight mb-6 sm:mb-7 drop-shadow-xl transition-all duration-300">
          <span class="text-[#f97316]">Optimos</span><span class="text-white">Store</span>
        </h1>

        <form onsubmit="handleSearchSubmit(event)" class="w-full">
          <div class="w-full flex items-center bg-[#1e2634]/95 backdrop-blur-md border border-[#374151] focus-within:border-[#f97316] focus-within:ring-2 focus-within:ring-[#f97316]/25 rounded-xl overflow-hidden shadow-2xl transition">
            <input
              type="text"
              id="catalog-search"
              placeholder="Pesquisar qualquer produto, remédio, eletrônico, carro..."
              autocomplete="off"
              class="w-full bg-transparent text-slate-100 placeholder-slate-400 text-sm sm:text-base px-4 py-3 outline-none"
            />
            <button
              type="button"
              id="btn-clear-input"
              onclick="clearSearchResults()"
              title="Limpar pesquisa"
              class="hidden text-slate-400 hover:text-white px-2.5 py-2 text-xs font-bold cursor-pointer transition"
            >
              ✕
            </button>
            <button
              type="submit"
              id="btn-search-submit"
              aria-label="Pesquisar com Inteligência Artificial"
              class="h-12 px-4 sm:px-5 border-l border-[#374151] bg-[#252f3f]/95 hover:bg-[#f97316] text-slate-300 hover:text-white flex items-center justify-center gap-2 transition cursor-pointer shrink-0"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.1" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </form>
      </div>

      <div id="ai-research-workspace" class="hidden w-full max-w-5xl mx-auto mt-6 space-y-5 pb-12 animate-modal">
        <div class="bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl px-4 py-3 flex flex-wrap items-center justify-between gap-3 shadow-xl">
          <div class="flex items-center gap-2.5 min-w-0">
            <span class="w-2.5 h-2.5 rounded-full bg-[#f97316] animate-pulse shrink-0"></span>
            <div class="text-xs sm:text-sm text-slate-300 truncate">
              Análise OptimosIA conectada à web para: <strong id="search-query-label" class="text-[#f97316]"></strong>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button
              type="button"
              onclick="openPriceListModal()"
              class="bg-[#182032] hover:bg-slate-800 border border-slate-700 text-slate-200 text-xs font-semibold px-3 py-1.5 rounded-xl transition cursor-pointer flex items-center gap-1.5"
            >
              <span>Minha Lista</span>
              <span id="results-cart-count" class="bg-[#f97316] text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full">0</span>
            </button>
            <button
              type="button"
              onclick="clearSearchResults()"
              class="bg-[#182032] hover:bg-red-500/15 hover:text-red-300 hover:border-red-500/40 border border-slate-700 text-slate-300 text-xs font-semibold px-3 py-1.5 rounded-xl transition cursor-pointer"
            >
              Nova Busca ✕
            </button>
          </div>
        </div>

        <div id="ai-loading-state" class="hidden bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-8 text-center space-y-4 shadow-2xl">
          <div class="w-12 h-12 mx-auto rounded-2xl bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white shadow-lg shadow-orange-500/30 ai-pulse">
            <svg class="w-6 h-6 animate-spin" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </div>
          <div class="space-y-1">
            <h3 class="text-base sm:text-lg font-extrabold text-white">Consultando fontes oficiais e lojas em tempo real...</h3>
            <p class="text-xs sm:text-sm text-slate-400 max-w-md mx-auto">
              A IA do OptimosStore está extraindo a ficha técnica real, verificando registros oficiais (como Anvisa/fabricantes) e calculando a relação preço × qualidade.
            </p>
          </div>
        </div>

        <div id="ai-results-body" class="hidden space-y-5">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
            <div class="lg:col-span-7 bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-2xl flex flex-col justify-between space-y-4">
              <div class="space-y-3">
                <div class="flex flex-wrap items-start justify-between gap-3 pb-3.5 border-b border-slate-800">
                  <div class="space-y-1">
                    <div class="flex items-center gap-2">
                      <span class="w-2 h-2 rounded-full bg-[#f97316]"></span>
                      <span id="product-category-badge" class="text-[11px] font-bold uppercase tracking-wider text-[#f97316]">Ficha Técnica Real</span>
                    </div>
                    <h2 id="product-official-title" class="text-lg sm:text-xl font-extrabold text-white leading-snug">
                      Produto Pesquisado
                    </h2>
                    <p id="product-short-desc" class="text-xs text-slate-400 leading-relaxed">
                      Resumo técnico verificado.
                    </p>
                  </div>

                  <a
                    id="official-source-link"
                    href="https://consultas.anvisa.gov.br/#/bulario/"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="inline-flex items-center gap-2 bg-[#f97316] hover:bg-[#e67e22] text-white px-4 py-2.5 rounded-xl text-xs font-bold transition shadow-lg shadow-orange-500/20 shrink-0"
                  >
                    <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                    <span id="official-source-label">Portal Oficial Anvisa (Bulário)</span>
                    <svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </a>
                </div>

                <div>
                  <div class="text-xs font-bold text-slate-300 mb-2.5 flex items-center justify-between">
                    <span>Especificações & Dados Técnicos</span>
                    <span id="regulatory-note-badge" class="hidden text-[10px] bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 px-2 py-0.5 rounded-full font-semibold">
                      Registro Sanitário / Anvisa
                    </span>
                  </div>
                  <div id="tech-specs-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5"></div>
                </div>
              </div>

              <div id="grounding-sources-box" class="hidden pt-3 border-t border-slate-800/80">
                <div class="text-[11px] font-semibold text-slate-400 mb-1.5">Referências consultadas na web:</div>
                <div id="grounding-sources-list" class="flex flex-wrap gap-1.5"></div>
              </div>
            </div>

            <div class="lg:col-span-5 bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-2xl flex flex-col justify-between space-y-4">
              <div class="space-y-4">
                <div class="flex items-center justify-between gap-2 pb-3 border-b border-slate-800">
                  <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-[#f97316]"></span>
                    <h3 class="font-extrabold text-white text-sm sm:text-base">Ficha de Preços & Veredito</h3>
                  </div>
                  <span id="price-trend-badge" class="text-[11px] font-bold px-2.5 py-1 rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                    Está barato agora
                  </span>
                </div>

                <div id="combo-verdict-card" class="rounded-xl p-4 border bg-[#182032] border-[#f97316]/40 space-y-1.5">
                  <div class="flex items-center justify-between gap-2">
                    <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Classificação Combinada</span>
                    <span id="combo-score-pill" class="text-xs font-black text-[#f97316]">9.2 / 10</span>
                  </div>
                  <div id="combo-verdict-title" class="text-base sm:text-lg font-black text-white">
                    Barato e Bom • Excelente Custo-Benefício
                  </div>
                  <p id="combo-verdict-reason" class="text-xs text-slate-300 leading-relaxed">
                    Análise detalhada da relação entre o preço praticado atualmente e a qualidade técnica entregue.
                  </p>
                </div>

                <div class="grid grid-cols-3 gap-2 text-center">
                  <div class="bg-[#182032] border border-emerald-500/30 rounded-xl p-2.5">
                    <div class="text-[10px] font-bold text-emerald-400 uppercase">Menor Preço</div>
                    <div id="price-min-val" class="text-xs sm:text-sm font-black text-white mt-1">R$ 0,00</div>
                  </div>
                  <div class="bg-[#182032] border border-slate-700 rounded-xl p-2.5">
                    <div class="text-[10px] font-bold text-slate-400 uppercase">Preço Médio</div>
                    <div id="price-avg-val" class="text-xs sm:text-sm font-black text-slate-200 mt-1">R$ 0,00</div>
                  </div>
                  <div class="bg-[#182032] border border-red-500/25 rounded-xl p-2.5">
                    <div class="text-[10px] font-bold text-red-400 uppercase">Maior Preço</div>
                    <div id="price-max-val" class="text-xs sm:text-sm font-black text-slate-300 mt-1">R$ 0,00</div>
                  </div>
                </div>

                <div class="space-y-2.5 pt-1">
                  <div>
                    <div class="flex justify-between text-[11px] font-semibold mb-1">
                      <span class="text-slate-300">Qualidade Técnica / Eficácia</span>
                      <span id="meter-quality-label" class="text-emerald-400 font-bold">Muito Bom (88%)</span>
                    </div>
                    <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                      <div id="meter-quality-bar" class="h-full bg-emerald-500 rounded-full transition-all duration-500" style="width: 88%"></div>
                    </div>
                  </div>

                  <div>
                    <div class="flex justify-between text-[11px] font-semibold mb-1">
                      <span class="text-slate-300">Acessibilidade do Preço</span>
                      <span id="meter-price-label" class="text-[#f97316] font-bold">Barato (82%)</span>
                    </div>
                    <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                      <div id="meter-price-bar" class="h-full bg-[#f97316] rounded-full transition-all duration-500" style="width: 82%"></div>
                    </div>
                  </div>

                  <div>
                    <div class="flex justify-between text-[11px] font-semibold mb-1">
                      <span class="text-slate-300">Índice de Custo-Benefício</span>
                      <span id="meter-cb-label" class="text-sky-400 font-bold">Excelente (91%)</span>
                    </div>
                    <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                      <div id="meter-cb-bar" class="h-full bg-sky-400 rounded-full transition-all duration-500" style="width: 91%"></div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="pt-3 border-t border-slate-800 flex items-center gap-2">
                <button
                  type="button"
                  id="btn-save-analyzed-product"
                  onclick="saveAnalyzedProductToCart()"
                  class="flex-1 bg-[#e67e22] hover:bg-[#f97316] text-white font-bold text-xs py-2.5 px-3 rounded-xl shadow-lg shadow-orange-500/20 transition cursor-pointer"
                >
                  + Salvar na Lista de Preços
                </button>
                <button
                  type="button"
                  id="btn-alert-analyzed-product"
                  onclick="createAlertForAnalyzedProduct()"
                  class="bg-[#182032] hover:bg-slate-800 border border-slate-700 text-orange-300 font-bold text-xs py-2.5 px-3.5 rounded-xl transition cursor-pointer"
                >
                  Criar Alerta
                </button>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
            <div class="lg:col-span-5 bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-5 shadow-xl space-y-4">
              <h3 class="font-extrabold text-white text-sm flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-[#f97316]"></span>
                Pontos Positivos & Pontos de Atenção
              </h3>

              <div class="space-y-3">
                <div class="bg-emerald-950/20 border border-emerald-500/25 rounded-xl p-3.5">
                  <div class="text-xs font-bold text-emerald-400 mb-2">✓ Pontos Fortes (O que é Bom)</div>
                  <ul id="product-pros-list" class="space-y-1.5 text-xs text-slate-300"></ul>
                </div>

                <div class="bg-red-950/20 border border-red-500/25 rounded-xl p-3.5">
                  <div class="text-xs font-bold text-red-400 mb-2">! Pontos de Atenção / Contras</div>
                  <ul id="product-cons-list" class="space-y-1.5 text-xs text-slate-300"></ul>
                </div>
              </div>
            </div>

            <div class="lg:col-span-7 bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-5 shadow-xl space-y-3.5">
              <div class="flex items-center justify-between gap-2">
                <h3 class="font-extrabold text-white text-sm flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-[#f97316]"></span>
                  Comparativo de Ofertas & Lojas Verificadas
                </h3>
                <span class="text-[11px] text-slate-400">Ordenado do menor para o maior preço</span>
              </div>

              <div id="offers-comparison-list" class="space-y-2.5"></div>
            </div>
          </div>

          <div class="bg-[#111827]/95 backdrop-blur-md border border-slate-800 rounded-2xl p-5 shadow-2xl space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
              <div class="flex items-center gap-2.5">
                <div class="w-8 h-8 rounded-xl bg-gradient-to-br from-[#f59e0b] to-[#e67e22] flex items-center justify-center text-white shadow">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                  </svg>
                </div>
                <div>
                  <h3 class="font-extrabold text-white text-sm">Assistente Inteligente OptimosIA</h3>
                  <p class="text-[11px] text-slate-400">Tire dúvidas técnicas, compare alternativas ou pergunte se vale a pena comprar agora</p>
                </div>
              </div>

              <div class="flex flex-wrap gap-1.5">
                <button type="button" onclick="askFollowUpSuggestion('Quais são os melhores concorrentes diretos com melhor custo-benefício?')" class="bg-[#182032] hover:bg-slate-800 border border-slate-700 text-slate-300 hover:text-orange-300 text-[11px] px-2.5 py-1 rounded-lg transition cursor-pointer">
                  Comparar concorrentes
                </button>
                <button type="button" onclick="askFollowUpSuggestion('Vale a pena comprar pelo menor preço atual ou esperar promoção?')" class="bg-[#182032] hover:bg-slate-800 border border-slate-700 text-slate-300 hover:text-orange-300 text-[11px] px-2.5 py-1 rounded-lg transition cursor-pointer">
                  Vale a pena agora?
                </button>
              </div>
            </div>

            <div id="ai-chat-history" class="space-y-3 max-h-72 overflow-y-auto pr-1"></div>

            <form onsubmit="handleFollowUpQuestion(event)" class="flex items-center gap-2">
              <input
                type="text"
                id="ai-followup-input"
                placeholder="Pergunte qualquer coisa sobre este produto à OptimosIA..."
                class="flex-1 bg-[#182032] border border-slate-700 focus:border-[#f97316] text-slate-100 placeholder-slate-500 text-xs sm:text-sm px-3.5 py-2.5 rounded-xl outline-none transition"
              />
              <button
                type="submit"
                id="btn-followup-send"
                class="bg-[#e67e22] hover:bg-[#f97316] text-white font-bold text-xs sm:text-sm px-4 py-2.5 rounded-xl shadow transition cursor-pointer shrink-0"
              >
                Perguntar
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer id="main-footer" class="relative z-10 w-full py-6 px-4 mt-auto text-center space-y-1.5">
    <p class="text-[11px] sm:text-xs text-slate-500">
      As ofertas exibidas no OptimosStore são pesquisadas em lojas parceiras — verifique sempre as condições finais antes de concluir sua compra.
    </p>
  </footer>

const DATASETS = [
  // ===== American Sign Language (ASL) =====
  { name: "MS-ASL", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "25,121 videos, 1,000 classes", license: "Research Use", source: "https://www.microsoft.com/en-us/research/project/ms-asl/", desc: "Large-scale real-life ASL dataset from Microsoft with 222 signers.", citation: "Vaezi Joze et al., AAAI 2019" },
  { name: "WLASL", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "21,083 videos, 2,000 classes", license: "CC BY 4.0", source: "https://github.com/dxli94/WLASL", desc: "Word-level ASL recognition dataset with 100+ signers.", citation: "Li et al., WACV 2020" },
  { name: "How2Sign", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "80+ hours continuous", license: "CC BY-NC 4.0", source: "https://how2sign.github.io/", desc: "Large-scale multimodal continuous ASL with multiview, depth, and pose.", citation: "Duarte et al., CVPR 2021" },
  { name: "OpenASL", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "284+ hours, 200+ signers", license: "CC BY-NC 4.0", source: "https://github.com/chevalierNoir/OpenASL", desc: "Open-domain continuous ASL translation from online videos.", citation: "Shi et al., EMNLP 2022" },
  { name: "ASLLVD", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "~9,800 tokens, 3,300+ signs", license: "Research Use", source: "https://www.bu.edu/asllrp/av/dai-asllvd.html", desc: "Multi-angle ASL lexicon video dataset from Boston University.", citation: "Athitsos et al., CVPR Workshop 2008" },
  { name: "YouTube-ASL", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "11,093 videos, 984 hours", license: "Research Use", source: "https://github.com/google-research/google-research/tree/master/youtube_asl", desc: "Large-scale open-domain ASL-English parallel corpus from Google Research.", citation: "Uthus et al., 2023" },
  { name: "ASL-MNIST", language: "ASL", languageFull: "American Sign Language", modality: "Image", samples: "34,627 images, 24 classes", license: "CC BY-SA 4.0", source: "https://www.kaggle.com/datasets/datamunge/sign-language-mnist", desc: "Grayscale 28×28 ASL alphabet images in MNIST format.", citation: "Kaggle community" },
  { name: "ASL Alphabet", language: "ASL", languageFull: "American Sign Language", modality: "Image", samples: "87,000 images, 29 classes", license: "CC BY 4.0", source: "https://www.kaggle.com/datasets/grassknoted/asl-alphabet", desc: "200×200 RGB images of ASL alphabet including space, delete, nothing.", citation: "Kaggle community (grassknoted)" },
  { name: "ASL-LEX", language: "ASL", languageFull: "American Sign Language", modality: "Dictionary", samples: "~2,700+ signs", license: "CC BY 4.0", source: "https://asl-lex.org/", desc: "Lexical database with phonological features, frequency, and iconicity ratings.", citation: "Caselli et al., 2017" },
  { name: "ASL Citizen", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "Crowdsourced signs", license: "CC BY 4.0", source: "https://aslcitizen.org/", desc: "Multimodal dataset for Deaf-Hearing AI collaboration with diverse signers.", citation: "De Meulder et al., LREC 2022" },
  { name: "AUTSL (ASL benchmark)", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "38,336 videos, 226 signs", license: "CC BY 4.0", source: "https://arxiv.org/abs/2008.00932", desc: "Multi-modal Turkish Sign Language dataset also used as ASL benchmark.", citation: "Ciga et al., arXiv 2020" },
  { name: "ChaLearn LAP SLR Challenge", language: "ASL", languageFull: "American Sign Language", modality: "Video", samples: "36,302 samples", license: "Research Use", source: "https://chalearnlap.cvc.uab.cat/", desc: "Multi-modal sign language recognition challenge dataset (AUTSL subset).", citation: "Escalera et al., CVPRW 2021" },

  // ===== Arabic Sign Language (ArSL) =====
  { name: "ArSL2018", language: "ArSL", languageFull: "Arabic Sign Language", modality: "Image", samples: "54,049 images, 32 classes", license: "CC BY 4.0", source: "https://www.kaggle.com/datasets/ahmedkhan123/arabic-sign-language", desc: "Arabic sign language alphabet images from 40 signers.", citation: "Kaggle community" },
  { name: "KArSL-502", language: "ArSL", languageFull: "Arabic Sign Language", modality: "Video", samples: "502 signs", license: "Research Use", source: "https://huggingface.co/datasets/karlsruhe-nerdstation/karSL-502", desc: "Karlsruhe Arabic Sign Language recognition dataset.", citation: "See HuggingFace dataset card" },

  // ===== Australian Sign Language (Auslan) =====
  { name: "Auslan Signbank", language: "Auslan", languageFull: "Australian Sign Language", modality: "Dictionary", samples: "5,000+ signs", license: "CC BY-NC-SA 4.0", source: "https://auslan.org.au/", desc: "Comprehensive video dictionary with grammatical information.", citation: "Johnston & De Beuzeville, Macquarie University" },

  // ===== Bangla Sign Language (BdSL) =====
  { name: "BdSL47", language: "BdSL", languageFull: "Bangla Sign Language", modality: "Image", samples: "47,000 images, 47 classes", license: "CC BY 4.0", source: "https://zenodo.org/record/7067906", desc: "Complete Bangla sign alphabet and digits dataset from 10 signers.", citation: "Afzal et al., Zenodo 2022" },
  { name: "KU-BdSL", language: "BdSL", languageFull: "Bangla Sign Language", modality: "Image", samples: "4,500 images, 3 variants", license: "CC BY 4.0", source: "https://data.mendeley.com/datasets/scpvm2nbkm/1", desc: "Khulna University Bengali Sign Language with USLD, MSLD, AMSLD variants.", citation: "Islam et al., Mendeley Data 2023" },
  { name: "Ban-Sign-Sent-9K", language: "BdSL", languageFull: "Bangla Sign Language", modality: "Video", samples: "9,610 videos", license: "CC BY-NC 4.0", source: "https://huggingface.co/datasets/banglagov/Ban-Sign-Sent-9K-V1", desc: "Continuous Bangla sign language sentence-level videos.", citation: "See HuggingFace dataset card" },
  { name: "BdSL-Sensor-Glove", language: "BdSL", languageFull: "Bangla Sign Language", modality: "Sensor", samples: "4,824 recordings, 36 gestures", license: "CC BY 4.0", source: "data/bdsl/BdSL-Sensor-Glove/", desc: "Flex sensor + IMU glove data with 11 channels.", citation: "Included in repository" },

  // ===== Brazilian Sign Language (Libras) =====
  { name: "Libras-UFPR", language: "Libras", languageFull: "Brazilian Sign Language", modality: "Video", samples: "9,600+ video samples", license: "CC BY 4.0", source: "https://www.inf.ufpr.br/lesoliveira/libras/", desc: "Isolated Brazilian Sign Language sign videos from UFPR.", citation: "Oliveira et al., UFPR" },
  { name: "PHOENIX-Libras", language: "Libras", languageFull: "Brazilian Sign Language", modality: "Video", samples: "Continuous sentences", license: "Research Use", source: "Contact UFPR", desc: "Parallel corpus of Brazilian Sign Language with gloss annotations.", citation: "Moura et al., LREC 2022" },

  // ===== British Sign Language (BSL) =====
  { name: "BOBSL", language: "BSL", languageFull: "British Sign Language", modality: "Video", samples: "~1,400 hours, 1.2M sentences", license: "BBC License", source: "https://www.robots.ox.ac.uk/~vgg/data/bobsl/", desc: "BBC-Oxford BSL dataset from TV broadcasts with 37 signers.", citation: "Albanie et al., ECCV 2022" },
  { name: "BSL Corpus", language: "BSL", languageFull: "British Sign Language", modality: "Video", samples: "~160 hours", license: "Research Use", source: "https://bslcorpusproject.org/", desc: "Conversational British Sign Language corpus.", citation: "Schembri et al., 2011" },
  { name: "BSL SignBank", language: "BSL", languageFull: "British Sign Language", modality: "Dictionary", samples: "BSL signs with video", license: "Contact UCL DCAL", source: "https://bslsignbank.ucl.ac.uk/", desc: "BSL signs with video, gloss, and phonological features.", citation: "Fenlon et al., UCL" },

  // ===== Chinese Sign Language (CSL) =====
  { name: "DEVISIGN", language: "CSL", languageFull: "Chinese Sign Language", modality: "Video", samples: "24,000 videos, 2,000 words", license: "Research Use", source: "Contact CASIA", desc: "Large vocabulary isolated sign videos from 8 signers.", citation: "Li et al., ACM MM 2015" },
  { name: "USTC-CSL", language: "CSL", languageFull: "Chinese Sign Language", modality: "Video", samples: "Benchmark dataset", license: "Research Use", source: "Contact USTC", desc: "Chinese sign language recognition benchmark.", citation: "Huang et al., AAAI 2018" },

  // ===== Dutch Sign Language (NGT) =====
  { name: "CNGT Corpus", language: "NGT", languageFull: "Dutch Sign Language", modality: "Video", samples: "Spontaneous conversations", license: "Research Use", source: "https://www.ru.nl/cngt/", desc: "Corpus of spontaneous Dutch Sign Language conversations.", citation: "Crasborn et al., 2022" },

  // ===== French Sign Language (LSF) =====
  { name: "Dicta-Sign LSF", language: "LSF", languageFull: "French Sign Language", modality: "Video", samples: "French SL recordings", license: "Research Use", source: "EU Dicta-Sign Project", desc: "French Sign Language recordings from the EU Dicta-Sign project.", citation: "Mattheyses et al., LREC 2012" },
  { name: "LSF-Dict", language: "LSF", languageFull: "French Sign Language", modality: "Dictionary", samples: "Video dictionary", license: "Community", source: "https://www.lsf-dict.fr/", desc: "French Sign Language dictionary maintained by the Deaf community.", citation: "French Deaf community" },

  // ===== German Sign Language (DGS) =====
  { name: "RWTH-PHOENIX-Weather 2014", language: "DGS", languageFull: "German Sign Language", modality: "Video", samples: "6,841 sentences, 9 signers", license: "Research Use", source: "https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/", desc: "Benchmark continuous sign language recognition from weather forecasts.", citation: "Koller et al., CVIU 2015" },
  { name: "RWTH-PHOENIX-Weather 2014T", language: "DGS", languageFull: "German Sign Language", modality: "Video", samples: "8,257 sentences (39GB)", license: "Research Use", source: "https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX-2014-T/", desc: "Extended PHOENIX with German glosses and spoken language transcriptions.", citation: "Camgöz et al., CVPR 2018" },
  { name: "DGS Corpus", language: "DGS", languageFull: "German Sign Language", modality: "Video", samples: "Large-scale annotated corpus", license: "Research Use", source: "https://www.sign-lang.uni-hamburg.de/dgs-korpus/", desc: "Large-scale German Sign Language corpus with gloss annotations.", citation: "König et al., Hamburg University" },

  // ===== Greek Sign Language (GSL) =====
  { name: "GSL-50", language: "GSL", languageFull: "Greek Sign Language", modality: "Video", samples: "Sign vocabulary", license: "Research Use", source: "Contact University of Athens", desc: "Greek Sign Language sign vocabulary dataset with audio.", citation: "University of Athens" },

  // ===== Indian Sign Language (ISL) =====
  { name: "INCLUDE", language: "ISL", languageFull: "Indian Sign Language", modality: "Video", samples: "38,640 videos, 263 classes", license: "Research Use", source: "https://signlanguage-iisc.github.io/", desc: "Large-scale Indian Sign Language recognition dataset from IISc Bangalore.", citation: "Sridhar et al., ACM MM 2020" },
  { name: "ISL-CSLTR", language: "ISL", languageFull: "Indian Sign Language", modality: "Video", samples: "Sentence-level continuous", license: "CC BY 4.0", source: "https://data.mendeley.com/datasets/kcmpdxky7p/1", desc: "Indian Sign Language continuous sign language translation with gloss annotations.", citation: "Jadhav et al., Mendeley Data" },
  { name: "ISL-Alphabet", language: "ISL", languageFull: "Indian Sign Language", modality: "Image", samples: "12,700 images", license: "CC BY 4.0", source: "https://github.com/ayeshatasnim-h/Indian-Sign-Language-dataset", desc: "Indian Sign Language alphabet sign images.", citation: "Tasnim, 2021" },

  // ===== Irish Sign Language (ISL) =====
  { name: "ISL Corpus", language: "ISL", languageFull: "Irish Sign Language", modality: "Video", samples: "Conversations & narratives", license: "Research Use", source: "https://www.islc.ie/", desc: "Corpus of Irish Sign Language conversations and narratives.", citation: "Le Master et al., Trinity College Dublin" },

  // ===== Italian Sign Language (LIS) =====
  { name: "ATIS", language: "LIS", languageFull: "Italian Sign Language", modality: "Video", samples: "Annotated dataset", license: "Research Use", source: "Contact University of Bologna", desc: "Italian Sign Language dataset with annotations.", citation: "Cavazza et al., University of Bologna" },

  // ===== Japanese Sign Language (JSL) =====
  { name: "J-ASL", language: "JSL", languageFull: "Japanese Sign Language", modality: "Video", samples: "Lexicon dataset", license: "Research Use", source: "Contact NICT/JSPS", desc: "Japanese Sign Language lexicon with linguistic annotations.", citation: "Japanese NLP/SLR research groups" },

  // ===== Korean Sign Language (KSL) =====
  { name: "KETI Sign Language", language: "KSL", languageFull: "Korean Sign Language", modality: "Video", samples: "Weather forecast data", license: "Research Use", source: "Contact ETRI Korea", desc: "Korean weather forecast sign language data.", citation: "ETRI Korea" },

  // ===== Malaysian Sign Language (BIM) =====
  { name: "MSL Dataset", language: "BIM", languageFull: "Malaysian Sign Language", modality: "Image", samples: "Sign images", license: "CC BY 4.0", source: "https://huggingface.co/datasets/sayedeh/Malaysian-Sign-Language-Dataset", desc: "Malaysian Sign Language sign images for recognition.", citation: "See HuggingFace dataset card" },

  // ===== Mexican Sign Language (LSM) =====
  { name: "LSM Dataset", language: "LSM", languageFull: "Mexican Sign Language", modality: "Image", samples: "Alphabet & word signs", license: "Research Use", source: "Available on Kaggle", desc: "Mexican Sign Language alphabet and word sign images/videos.", citation: "Mexican research institutions" },

  // ===== Russian Sign Language (RSL) =====
  { name: "RuSLAN Collection", language: "RSL", languageFull: "Russian Sign Language", modality: "Video", samples: "Sign dataset", license: "CC BY 4.0", source: "https://russian-sign-language.github.io/", desc: "Russian Sign Language dataset for recognition.", citation: "RuSLAN project" },
  { name: "RSL-Signs", language: "RSL", languageFull: "Russian Sign Language", modality: "Video", samples: "Signs collection", license: "CC BY 4.0", source: "GitHub", desc: "Russian Sign Language signs collection.", citation: "HSE Moscow" },

  // ===== Swedish Sign Language (SSL) =====
  { name: "SSL Corpus", language: "SSL", languageFull: "Swedish Sign Language", modality: "Video", samples: "Corpus with annotations", license: "Research Use", source: "https://www.ling.su.se/ssl/", desc: "Swedish Sign Language corpus from Stockholm University.", citation: "Mesch et al., 2012" },

  // ===== Thai Sign Language (TSL) =====
  { name: "TSL-51", language: "TSL", languageFull: "Thai Sign Language", modality: "Image", samples: "Alphabet dataset", license: "CC BY 4.0", source: "https://huggingface.co/datasets/nodtcotai/tsl-51", desc: "Thai Sign Language alphabet recognition dataset.", citation: "See HuggingFace dataset card" },

  // ===== Turkish Sign Language (TİD) =====
  { name: "AUTSL", language: "TİD", languageFull: "Turkish Sign Language", modality: "Video", samples: "38,336 videos, 226 signs", license: "CC BY 4.0", source: "https://arxiv.org/abs/2008.00932", desc: "Large-scale multi-modal Turkish Sign Language with RGB-D and skeleton.", citation: "Ciga et al., arXiv 2020" },

  // ===== Multilingual & Cross-lingual =====
  { name: "SIGN-Hub", language: "Multi", languageFull: "Multilingual", modality: "Video", samples: "ASL, BSL, DGS, LSF, GSL, ISL, Libras", license: "Research Use", source: "https://www.sign-hub.eu/", desc: "EU-funded corpus + annotation tools for multiple European sign languages.", citation: "Hanke et al., LREC 2016" },
  { name: "Dicta-Sign", language: "Multi", languageFull: "Multilingual", modality: "Video", samples: "4,000+ videos, 4 languages", license: "Research Use", source: "EU Dicta-Sign Project", desc: "Multilingual sign language corpus: BSL, DGS, GSL, LSF.", citation: "Mattheyses et al., LREC 2012" },
  { name: "SpreadTheSign", language: "Multi", languageFull: "Multilingual", modality: "Dictionary", samples: "500,000+ signs, 30+ languages", license: "Permission required", source: "https://www.spreadthesign.com/", desc: "Global multilingual sign language dictionary from the European Sign Language Centre.", citation: "European Sign Language Centre" },
  { name: "OpenSLR", language: "Multi", languageFull: "Multilingual", modality: "Video", samples: "Varies per resource", license: "Varies", source: "https://www.openslr.org/", desc: "Repository of speech and language resources including some sign language.", citation: "Varies per resource" },
  { name: "SLP Toolkit", language: "Multi", languageFull: "Multilingual", modality: "Video", samples: "Preprocessed datasets", license: "Varies", source: "https://www.sign-language-processing.com/", desc: "Preprocessed sign language datasets for ML research (ASL, DGS, BSL, etc.).", citation: "See project documentation" },

  // ===== NEW: Additional verified datasets =====
  { name: "SignAvatars", language: "Multi", languageFull: "Multilingual", modality: "Video", samples: "8.34M 3D annotations, 70K sequences", license: "Research Use", source: "https://github.com/ZhengdiYu/SignAvatars", desc: "First large-scale 3D sign language holistic motion dataset with SMPL-X mesh annotations.", citation: "Yu et al., ECCV 2024" },
  { name: "Sign Language 26", language: "ASL", languageFull: "American Sign Language", modality: "Image", samples: "18,200 images, 15 classes", license: "Community", source: "https://huggingface.co/datasets/Gsco-HF/sign-language-26", desc: "ASL sign language image dataset with 15 classes at 1280×1280.", citation: "Gsco-HF, HuggingFace" },
  { name: "Pakistani Sign Language (PSL)", language: "PSL", languageFull: "Pakistani Sign Language", modality: "Sensor", samples: "Landmark-based gestures", license: "CC BY 4.0", source: "https://huggingface.co/datasets/Bakhtyar12/Pakistani-Sign-Language", desc: "MediaPipe-based PSL gesture recognition dataset covering alphabets, words, and sentences.", citation: "Bakhtyar12, HuggingFace" },
  { name: "Marathi Sign Language", language: "MSL", languageFull: "Marathi Sign Language", modality: "Image", samples: "50,100+ images, 43 classes", license: "Community", source: "https://huggingface.co/datasets/VinayHajare/Marathi-Sign-Language", desc: "Marathi sign language alphabet detection dataset at 128×128 pixels.", citation: "VinayHajare, HuggingFace" },
  { name: "Nigerian Sign Language Corpus", language: "NSL", languageFull: "Nigerian Sign Language", modality: "Video", samples: "5,250+ samples", license: "Research Use", source: "https://huggingface.co/datasets/Lanfrica/sign-to-speech-for-sign-language-understanding-a-case-study-of-nigerian-sign-language", desc: "Sign-to-speech corpus for Nigerian Sign Language understanding.", citation: "Lanfrica, HuggingFace" },
  { name: "Ghanaian Sign Language Lexicon", language: "GSL", languageFull: "Ghanaian Sign Language", modality: "Video", samples: "Lexicon dataset", license: "Community", source: "https://huggingface.co/datasets/jameszokah/ghanaian-sign-language-lexicon", desc: "Ghanaian Sign Language lexicon with landmark annotations.", citation: "jameszokah, HuggingFace" },
];

const MODALITY_MAP = {
  "Video": "video", "Image": "image", "Sensor": "sensor",
  "Dictionary": "dict", "Video": "video"
};

function getModalityBadge(modality) {
  const m = modality.toLowerCase();
  if (m.includes("video")) return "video";
  if (m.includes("image")) return "image";
  if (m.includes("sensor")) return "sensor";
  if (m.includes("dict")) return "dict";
  if (m.includes("multi")) return "multi";
  if (m.includes("corpus")) return "corpus";
  return "video";
}

function getLicenseClass(license) {
  if (license.includes("CC BY")) return "open";
  if (license.includes("Research")) return "research";
  return "other";
}

// Get unique languages
const languages = [...new Set(DATASETS.map(d => d.language))].sort();
const modalities = [...new Set(DATASETS.map(d => {
  const m = d.modality.toLowerCase();
  if (m.includes("video") && m.includes("image")) return "Multi";
  if (m.includes("video")) return "Video";
  if (m.includes("image")) return "Image";
  if (m.includes("sensor")) return "Sensor";
  if (m.includes("dict")) return "Dictionary";
  return d.modality;
}))];

let currentLanguage = "All";
let currentModality = "All";
let currentSearch = "";

function filterDatasets() {
  return DATASETS.filter(d => {
    if (currentLanguage !== "All" && d.language !== currentLanguage) return false;
    if (currentModality !== "All") {
      const m = d.modality.toLowerCase();
      const cm = currentModality.toLowerCase();
      if (cm === "video" && !m.includes("video")) return false;
      if (cm === "image" && !m.includes("image")) return false;
      if (cm === "sensor" && !m.includes("sensor")) return false;
      if (cm === "dictionary" && !m.includes("dict")) return false;
    }
    if (currentSearch) {
      const q = currentSearch.toLowerCase();
      return d.name.toLowerCase().includes(q)
        || d.language.toLowerCase().includes(q)
        || d.languageFull.toLowerCase().includes(q)
        || d.modality.toLowerCase().includes(q)
        || d.desc.toLowerCase().includes(q);
    }
    return true;
  });
}

function renderCards(datasets) {
  const grid = document.getElementById("dataset-grid");
  const countEl = document.getElementById("results-count");

  if (datasets.length === 0) {
    grid.innerHTML = `<div class="no-results"><div class="icon">🔍</div>No datasets found matching your filters.</div>`;
    countEl.textContent = "0 datasets";
    return;
  }

  countEl.textContent = `${datasets.length} dataset${datasets.length !== 1 ? "s" : ""}`;

  grid.innerHTML = datasets.map(d => `
    <div class="dataset-card">
      <div class="card-header">
        <div class="card-title">${escapeHtml(d.name)}</div>
        <span class="card-language">${escapeHtml(d.language)}</span>
      </div>
      <div class="card-badges">
        <span class="badge badge-${getModalityBadge(d.modality)}">${escapeHtml(d.modality)}</span>
        <span class="badge badge-${getLicenseClass(d.license) === 'open' ? 'image' : getLicenseClass(d.license) === 'research' ? 'corpus' : 'dict'}">${escapeHtml(d.license)}</span>
      </div>
      <div class="card-desc">${escapeHtml(d.desc)}</div>
      <div class="card-meta">
        <span class="card-samples">📊 ${escapeHtml(d.samples)}</span>
        <a href="${escapeHtml(d.source)}" target="_blank" rel="noopener" class="card-source">🔗 Source</a>
      </div>
    </div>
  `).join("");
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

// Init
document.addEventListener("DOMContentLoaded", () => {
  // Render language tabs
  const tabsContainer = document.getElementById("lang-tabs");
  tabsContainer.innerHTML = `<button class="lang-tab active" data-lang="All">All</button>` +
    languages.map(l => `<button class="lang-tab" data-lang="${escapeHtml(l)}">${escapeHtml(l)}</button>`).join("");

  // Render modality dropdown
  const modalitySelect = document.getElementById("modality-filter");
  modalitySelect.innerHTML = `<option value="All">All Modalities</option>` +
    modalities.map(m => `<option value="${escapeHtml(m)}">${escapeHtml(m)}</option>`).join("");

  // Search
  document.getElementById("search-input").addEventListener("input", e => {
    currentSearch = e.target.value;
    renderCards(filterDatasets());
  });

  // Language tabs
  tabsContainer.addEventListener("click", e => {
    const tab = e.target.closest(".lang-tab");
    if (!tab) return;
    tabsContainer.querySelectorAll(".lang-tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");
    currentLanguage = tab.dataset.lang;
    renderCards(filterDatasets());
  });

  // Modality filter
  modalitySelect.addEventListener("change", e => {
    currentModality = e.target.value;
    renderCards(filterDatasets());
  });

  // Theme toggle
  const themeBtn = document.getElementById("theme-toggle");
  const saved = localStorage.getItem("theme");
  if (saved === "dark" || (!saved && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
    document.documentElement.setAttribute("data-theme", "dark");
    themeBtn.textContent = "☀️";
  }
  themeBtn.addEventListener("click", () => {
    const isDark = document.documentElement.getAttribute("data-theme") === "dark";
    document.documentElement.setAttribute("data-theme", isDark ? "light" : "dark");
    themeBtn.textContent = isDark ? "🌙" : "☀️";
    localStorage.setItem("theme", isDark ? "light" : "dark");
  });

  // Scroll to top
  const scrollBtn = document.getElementById("scroll-top");
  window.addEventListener("scroll", () => {
    scrollBtn.classList.toggle("visible", window.scrollY > 400);
  });
  scrollBtn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  // Accordion
  document.querySelectorAll(".accordion-header").forEach(header => {
    header.addEventListener("click", () => {
      const body = header.nextElementSibling;
      const isOpen = body.classList.contains("open");
      // Close all
      document.querySelectorAll(".accordion-body").forEach(b => b.classList.remove("open"));
      document.querySelectorAll(".accordion-header").forEach(h => h.classList.remove("open"));
      if (!isOpen) {
        body.classList.add("open");
        header.classList.add("open");
      }
    });
  });

  // Initial render
  renderCards(filterDatasets());
});

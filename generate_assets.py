import html
import os
import random
import textwrap

# ── 1. HAWK ASCII ART (Mangal Singh's Avatar Silhouette) ──────────────────────
HAWK_ASCII = [
    "      .---.                         ",
    "    _WWWWWWWWWWWW@%*                ",
    "   *WWWWWWWWWWW@%*...               ",
    "   WWWWWW%%W#WWWW:#oo               ",
    "   WWWWWWWWWWW%. #W.*.              ",
    " :*WWWW@WWW@@o    .:%+              ",
    "  :%W@@W:  [O]  . . .%+             ",
    "   <@%W+            #W+.            ",
    "   <% + .            @W+            ",
    "    \\                +*W            ",
    "     #W                W*           ",
    "      W#    +    .  *W +o           ",
    "     .W@:   +       Wo..            ",
    "      @W  .  * . W#   #WW           ",
    "      WW. @ WW #WW.++o:.            ",
    "     #WWWWo. W  +.W  W.  WWW        ",
    "     %WWoW W   W  . ::*W**#W        ",
    "     oW#Wo WW  W@.. .  +o           ",
    "      W%oW .W* WW+   :              ",
    "       #:%+ #W  W                   ",
    "        W.W  W  **                  ",
    "        W.WW  :o                    ",
    "        W:  o   +                   ",
    "        %@ %W WWW                   ",
    "        .@.WW%*WW.                  ",
    "        #W%WW+**+...                "
]

def make_line(y, key, val, max_len=58):
    prefix = f'. {key}: '
    suffix = f' {val}'
    # Adjust for HTML entity display lengths vs string lengths
    adjustment = 0
    if '&#x1F1EE;&#x1F1F3;' in val:
        adjustment += 14  # renders as 2 chars, string is 16
    if '&#x1F985;' in val:
        adjustment += 7   # renders as 1 char, string is 8
    dots_count = max_len - len(prefix) - len(suffix) + adjustment
    dots = '.' * max(1, dots_count)
    return f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">{key}</tspan>:<tspan class="cc"> {dots} </tspan><tspan class="value">{val}</tspan>'

def make_header(y, title, max_len=58):
    prefix = f'- {title} '
    dashes_count = max_len - len(prefix)
    dashes = '-' * max(1, dashes_count)
    return f'<tspan x="390" y="{y}">- {title} </tspan><tspan class="cc">{dashes}</tspan>'

def build_profile_svg(dark=True):
    bg    = "#161b22" if dark else "#f6f8fa"
    fg    = "#c9d1d9" if dark else "#24292f"
    key_c = "#ffa657" if dark else "#953800"
    val_c = "#a5d6ff" if dark else "#0a3069"
    add_c = "#3fb950" if dark else "#1a7f37"
    del_c = "#f85149" if dark else "#cf222e"
    cc_c  = "#616e7f" if dark else "#8c959f"
    stroke_c = "#30363d" if dark else "#d0d7de"

    # ASCII TSPANS
    ascii_tspans = "\n".join(
        f'<tspan x="20" y="{30 + i * 20}">{html.escape(ln)}</tspan>'
        for i, ln in enumerate(HAWK_ASCII)
    )

    # RIGHT INFO TSPANS
    y = 50
    lines = []
    lines.append(f'<tspan x="390" y="30" class="key">mangal@deeplearning-core</tspan> <tspan class="cc">---------------------------------------</tspan>')
    lines.append(make_line(y, 'OS', 'Linux (Ubuntu 24.04), Windows 11')); y += 20
    lines.append(make_line(y, 'Host', 'Neural-Engine v2.4 (NVIDIA CUDA)')); y += 20
    lines.append(make_line(y, 'Location', 'Bhopal, India &#x1F1EE;&#x1F1F3;')); y += 20
    lines.append(make_line(y, 'University', 'VIT Bhopal University (CSE AI/ML)')); y += 20
    lines.append(make_line(y, 'Role', 'AI/ML Engineer &amp; Systems Architect')); y += 30

    lines.append(make_line(y, 'Languages.Core', 'Python, C++, TypeScript, SQL, Java')); y += 20
    lines.append(make_line(y, 'AI.Frameworks', 'PyTorch, TensorFlow, OpenCV, MONAI')); y += 20
    lines.append(make_line(y, 'Systems.Deploy', 'FastAPI, Docker, TensorRT, ONNX')); y += 20
    lines.append(make_line(y, 'Research.Focus', 'Computer Vision, Space Debris, Edge-AI')); y += 20
    lines.append(make_line(y, 'Bio', 'Architecting AI tensor-to-edge &#x1F985;')); y += 30

    lines.append(make_header(y, 'Contact')); y += 20
    lines.append(make_line(y, 'Email', 'livingmangalsingh.02@gmail.com')); y += 20
    lines.append(make_line(y, 'LinkedIn', 'in/mangalsinghr')); y += 20
    lines.append(make_line(y, 'GitHub', 'livingmangal')); y += 20
    lines.append(make_line(y, 'Twitter/X', 'livingmangal')); y += 30

    lines.append(make_header(y, 'GitHub Stats')); y += 20
    lines.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value"> 19 {{Flagship: 4}}</tspan> <tspan class="cc">| </tspan><tspan class="key">Stars</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">  20+</tspan>'); y += 20
    lines.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">500+</tspan> <tspan class="cc">| </tspan><tspan class="key">Followers</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">   12</tspan>'); y += 20
    lines.append(f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">Lines of Code</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">186,420</tspan> ( <tspan class="addColor">214,830</tspan><tspan class="addColor">++</tspan>, <tspan class="delColor">28,410</tspan><tspan class="delColor">--</tspan> )')

    info_tspans = "\n".join(lines)

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="1030px" height="540px" font-size="15px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key   {{fill: {key_c}; font-weight: bold;}}
.value {{fill: {val_c};}}
.addColor {{fill: {add_c}; font-weight: bold;}}
.delColor {{fill: {del_c}; font-weight: bold;}}
.cc    {{fill: {cc_c};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="1030px" height="540px" fill="{bg}" rx="15" stroke="{stroke_c}" stroke-width="1.5"/>
<text x="20" y="30" fill="{fg}">
{ascii_tspans}
</text>
<text x="390" y="30" fill="{fg}">
{info_tspans}
</text>
</svg>"""


# ── 2. PROJECTS SHOWCASE SVG ──────────────────────────────────────────────────
PROJECTS = [
    {
        "name": "Synapse-OS",
        "badge": "⚡ AI Orchestrator",
        "desc": [
            "Production-grade Multilingual Public Health AI Orchestrator & Omnichannel Bot (WhatsApp/SMS).",
            "Features ABDM/ABHA EHR integration, SHA-256 Polygon blockchain verification, MONAI/YOLOv8",
            "clinical radiography, and WHO/IDSP real-time epidemic outbreak surveillance."
        ],
        "meta": "💻 Production Grade  |  📝 48,250 LOC  |  🚀 TypeScript • PyTorch • FastAPI • Polygon"
    },
    {
        "name": "Cosmic Recycler (debris_app)",
        "badge": "🛰️ Space Research",
        "desc": [
            "Machine Learning-driven Space Debris Classification and In-Orbit Metallurgical Recycling",
            "Framework for Orbital Sustainability (MDPI Research). Features computer vision object",
            "detection, satellite TLE trajectory tracking, and automated material classification."
        ],
        "meta": "💻 Research Paper  |  📝 18,500 LOC  |  🚀 Python • OpenCV • YOLO • TLE Tracking"
    },
    {
        "name": "Edge-AI-Earthquake-Detection",
        "badge": "📡 Edge Inference",
        "desc": [
            "Autonomous Edge AI prototype for earthquake early-warning using local sensor inference,",
            "peer verification mesh, and a high-throughput lightweight FastAPI pipeline. Optimized",
            "for minimal latency on embedded microcontrollers."
        ],
        "meta": "💻 Edge IoT Prototype  |  📝 12,400 LOC  |  🚀 Python • FastAPI • Edge AI • PyTorch"
    },
    {
        "name": "PostureAI-Hackathon",
        "badge": "👁️ Computer Vision",
        "desc": [
            "Real-time AI posture detection system leveraging webcam telemetry to evaluate ergonomics,",
            "deliver posture feedback, and drive long-term physical health through gamification and",
            "behavioral correction routines."
        ],
        "meta": "💻 Hackathon Build  |  📝 9,800 LOC  |  🚀 JavaScript • MediaPipe • React • Node.js"
    }
]

def build_projects_svg(dark=True):
    bg    = "#161b22" if dark else "#f6f8fa"
    fg    = "#c9d1d9" if dark else "#24292f"
    key_c = "#ffa657" if dark else "#953800"
    val_c = "#a5d6ff" if dark else "#0a3069"
    add_c = "#3fb950" if dark else "#1a7f37"
    cc_c  = "#616e7f" if dark else "#8c959f"
    stroke_c = "#30363d" if dark else "#d0d7de"

    y = 30
    tspans = [
        f'<tspan x="20" y="{y}" class="key">mangal@github</tspan> <tspan class="cc">---[ Featured Engineering &amp; Research Projects ]-----------------------</tspan>'
    ]
    y += 30

    for p in PROJECTS:
        tspans.append(f'<tspan x="20" y="{y}" class="cc">. </tspan><tspan class="add">📦 {p["name"]}</tspan> <tspan class="cc">[{p["badge"]}]</tspan>')
        y += 22
        for d in p["desc"]:
            tspans.append(f'<tspan x="20" y="{y}" class="cc">.    </tspan><tspan class="value">{html.escape(d)}</tspan>')
            y += 20
        tspans.append(f'<tspan x="20" y="{y}" class="cc">.    </tspan><tspan class="key">{html.escape(p["meta"])}</tspan>')
        y += 32

    total_height = y + 10

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="850px" height="{total_height}px" font-size="14.5px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key   {{fill: {key_c}; font-weight: bold;}}
.value {{fill: {val_c};}}
.add   {{fill: {add_c}; font-weight: bold;}}
.cc    {{fill: {cc_c};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="850px" height="{total_height}px" fill="{bg}" rx="12" stroke="{stroke_c}" stroke-width="1.5"/>
<text x="20" y="30" fill="{fg}">
{"\n".join(tspans)}
</text>
</svg>"""


# ── 3. DEV QUOTE SVG ──────────────────────────────────────────────────────────
QUOTES = [
    ("The ultimate goal of artificial intelligence is not to mimic human thought, but to extend the horizon of human capability.", "AI Philosophy"),
    ("Machine learning is not magic; it is mathematics, statistics, and domain intuition cast into rigorous code.", "Mangal Singh"),
    ("Simplicity is prerequisite for reliability. Complex neural pipelines require transparent engineering foundations.", "System Principle"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler")
]

def build_quote_svg(dark=True):
    bg    = "#161b22" if dark else "#f6f8fa"
    fg    = "#c9d1d9" if dark else "#24292f"
    key_c = "#ffa657" if dark else "#953800"
    val_c = "#a5d6ff" if dark else "#0a3069"
    cc_c  = "#616e7f" if dark else "#8c959f"
    stroke_c = "#30363d" if dark else "#d0d7de"

    quote_text, quote_author = QUOTES[0]
    wrapped = textwrap.wrap(f'"{quote_text}"', width=78)

    tspans = f'<tspan x="20" y="30" class="key">mangal@github</tspan> <tspan class="cc">---[ System Philosophy &amp; Quote ]------------------------------</tspan>\n'
    y = 60
    for line in wrapped:
        tspans += f'<tspan x="20" y="{y}" class="value">{html.escape(line)}</tspan>\n'
        y += 24

    author_str = f"- {quote_author}".rjust(78)
    tspans += f'<tspan x="20" y="{y + 8}" class="key">{html.escape(author_str)}</tspan>\n'
    total_height = y + 36

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="850px" height="{total_height}px" font-size="15px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key   {{fill: {key_c}; font-weight: bold;}}
.value {{fill: {val_c};}}
.cc    {{fill: {cc_c};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="850px" height="{total_height}px" fill="{bg}" rx="10" stroke="{stroke_c}" stroke-width="1.5"/>
<text x="20" y="30" fill="{fg}">
{tspans}
</text>
</svg>"""


# ── 4. AI CODING ACTIVITY / HACKATIME SVG ─────────────────────────────────────
def build_hackatime_svg(dark=True):
    bg    = "#161b22" if dark else "#f6f8fa"
    fg    = "#c9d1d9" if dark else "#24292f"
    key_c = "#ffa657" if dark else "#953800"
    val_c = "#a5d6ff" if dark else "#0a3069"
    cc_c  = "#616e7f" if dark else "#8c959f"
    stroke_c = "#30363d" if dark else "#d0d7de"

    col1 = [
        ("Python", "92h 40m"),
        ("PyTorch", "64h 15m"),
        ("TypeScript", "48h 20m"),
        ("C++", "35h 10m"),
        ("CUDA / C", "22h 30m"),
        ("FastAPI", "19h 45m"),
        ("OpenCV", "18h 12m"),
        ("SQL", "14h 50m")
    ]
    col2 = [
        ("Docker", "16h 30m"),
        ("JavaScript", "26h 15m"),
        ("ROS / Edge", "12h 40m"),
        ("TensorFlow", "21h 05m"),
        ("Linux / Bash", "11h 20m"),
        ("HTML / CSS", "15h 10m"),
        ("Markdown", "08h 45m"),
        ("Git / CI-CD", "07h 30m")
    ]

    tspans = f'<tspan x="20" y="30" class="key">mangal@github</tspan> <tspan class="cc">---[ AI &amp; Engineering Activity Metrics ]-------------------------</tspan>\n'
    y = 60
    for i in range(len(col1)):
        k1, v1 = col1[i]
        k2, v2 = col2[i]
        dots1 = "." * (14 - len(k1))
        dots2 = "." * (14 - len(k2))
        line = (
            f'<tspan x="20" y="{y}" class="cc">. </tspan>'
            f'<tspan class="key">{html.escape(k1)}</tspan>:<tspan class="cc"> {dots1} </tspan>'
            f'<tspan class="value">{v1.rjust(8)}</tspan>    <tspan class="cc">|    </tspan>'
            f'<tspan class="key">{html.escape(k2)}</tspan>:<tspan class="cc"> {dots2} </tspan>'
            f'<tspan class="value">{v2.rjust(8)}</tspan>\n'
        )
        tspans += line
        y += 24

    total_height = y + 20

    return f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="850px" height="{total_height}px" font-size="14.5px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key   {{fill: {key_c}; font-weight: bold;}}
.value {{fill: {val_c};}}
.cc    {{fill: {cc_c};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="850px" height="{total_height}px" fill="{bg}" rx="10" stroke="{stroke_c}" stroke-width="1.5"/>
<text x="20" y="30" fill="{fg}">
{tspans}
</text>
</svg>"""


def build_readme():
    skills_matrix = [
        ["python", "pytorch", "tensorflow", "opencv", "sklearn", "numpy", "pandas", "matlab", "r", "cpp", "c", "java"],
        ["fastapi", "flask", "django", "nodejs", "express", "react", "nextjs", "js", "ts", "html", "css", "tailwind"],
        ["postgres", "mysql", "mongodb", "sqlite", "redis", "kafka", "rabbitmq", "supabase", "firebase", "prisma", "graphql", "vite"],
        ["docker", "kubernetes", "aws", "gcp", "azure", "nginx", "grafana", "prometheus", "terraform", "cloudflare", "vercel", "netlify"],
        ["linux", "ubuntu", "bash", "powershell", "git", "github", "gitlab", "arduino", "raspberrypi", "rust", "go", "solidity"],
        ["vscode", "postman", "figma", "notion", "discord", "vim", "npm", "bun", "threejs", "bootstrap", "sass", "yarn"],
        ["cs", "dotnet", "vue", "svelte", "p5js", "md", "windows", "android", "apple", "jest", "babel", "pinia"]
    ]

    table_rows = ["<table>"]
    for r_idx, row in enumerate(skills_matrix):
        table_rows.append("  <tr>")
        for col_idx, s in enumerate(row):
            spacer = '<br><sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</sub>' if r_idx == 0 else ''
            table_rows.append(f'    <td width="80" align="center">\n      <img src="https://skillicons.dev/icons?i={s}&theme=dark" width="60" />{spacer}\n    </td>')
        table_rows.append("  </tr>")
    table_rows.append("</table>")
    skills_table_html = "\n".join(table_rows)

    readme_content = f"""<!-- Animated Header Banner -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=280&section=header&color=gradient&customColorList=6,11,20,28&text=Mangal%20Singh&fontSize=78&fontColor=ffffff&fontAlignY=40&desc=AI%20%7C%20Deep%20Learning%20Engineer%20%E2%80%A2%20Systems%20Architect%20%E2%80%A2%20Open%20Source%20Pioneer&descAlignY=62&descSize=19&animation=fadeIn" width="100%" alt="Header Banner" />
</div>

<!-- Typing SVG Animation -->
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=2600&pause=1000&color=58A6FF&center=true&vCenter=true&width=750&lines=Deep+Learning+%26+Neural+Architectures+%F0%9F%A4%96;Edge+AI+%7C+Autonomous+Inference+Engines+%E2%9A%A1;Production+Full-Stack+%26+Distributed+APIs+%F0%9F%9A%80;Space+Debris+%26+Biomedical+Vision+Research+%F0%9F%8C%8C;Architecting+the+Future+from+Tensor+to+Edge+%F0%9F%A6%85" alt="Typing SVG" />
</div>

<br/>

<!-- Neofetch Terminal Profile Card (Dual Theme Dark/Light) -->
<div align="center">
  <a href="https://github.com/livingmangal">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./dark_mode_v5.svg">
      <img alt="Mangal Singh's Terminal Profile README" src="./light_mode_v5.svg" width="100%">
    </picture>
  </a>
</div>

<br/>

<!-- Social & Connect Hub -->
<table align="center" width="100%">
  <tr>
    <td align="center" width="16%">
      <a href="https://www.linkedin.com/in/mangalsinghr/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
      </a>
    </td>
    <td align="center" width="16%">
      <a href="https://github.com/livingmangal" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
      </a>
    </td>
    <td align="center" width="16%">
      <a href="mailto:livingmangalsingh.02@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
      </a>
    </td>
    <td align="center" width="16%">
      <a href="https://twitter.com/livingmangal" target="_blank">
        <img src="https://img.shields.io/badge/Twitter/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="Twitter" />
      </a>
    </td>
    <td align="center" width="16%">
      <a href="https://huggingface.co" target="_blank">
        <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face" />
      </a>
    </td>
    <td align="center" width="16%">
      <a href="https://kaggle.com" target="_blank">
        <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle" />
      </a>
    </td>
  </tr>
</table>

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## 💀 Skills &amp; Stacks Arsenal

<div align="center">

{skills_table_html}

> *Trained on high-dimensional data, accelerated with CUDA kernels, and architected for mission-critical deployment.*

</div>

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## 📂 Featured Engineering &amp; Research Projects

<div align="center">

<table align="center" style="border: none;" width="100%">
  <tr>
    <td width="280" valign="top" align="center">
      <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop" width="100%" alt="AI Systems Architecture" style="border-radius: 12px; border: 1px solid #30363d;" />
      <br/><br/>
      <a href="https://github.com/livingmangal?tab=repositories">
        <img src="https://img.shields.io/badge/All%20Repositories-Explore%20Code-blue?style=for-the-badge&logo=github" alt="Explore All Repositories" />
      </a>
    </td>
    <td width="820" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./projects_dark_v1.svg?v=3">
        <img alt="Featured Projects" src="./projects_light_v1.svg?v=3" width="100%">
      </picture>
    </td>
  </tr>
</table>

</div>

<div align="center">

| 🚀 Project | 🏷️ Domain | 🛠️ Tech Stack | 🔗 Repository |
| :--- | :--- | :--- | :--- |
| **Synapse-OS** | Public Health AI Orchestrator | TypeScript • PyTorch • MONAI • YOLOv8 • Polygon | [View Project →](https://github.com/livingmangal/Synapse-OS) |
| **Cosmic Recycler** | Space Debris ML & Recycling (MDPI) | Python • OpenCV • YOLO • TLE Trajectory | [View Project →](https://github.com/livingmangal/debris_app) |
| **Edge-AI Earthquake** | Autonomous Seismic Warning Mesh | Python • FastAPI • Edge AI • PyTorch | [View Project →](https://github.com/livingmangal/Edge-AI-Earthquake-Detection-Project) |
| **PostureAI** | Computer Vision Ergonomics | JavaScript • MediaPipe • React • Node.js | [View Project →](https://github.com/livingmangal/PostureAI-Hackathon) |

</div>

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## 🧠 End-to-End AI &amp; Systems Architecture

```mermaid
graph LR
    subgraph Data["1. Data &amp; Telemetry Ingestion"]
        D1[Raw TLE Orbit Data] --> D2[Feature Extraction &amp; Preprocessing]
        D3[Clinical Radiography / DICOM] --> D2
        D4[Seismic Accelerometer Stream] --> D2
    end

    subgraph Modeling["2. Deep Learning &amp; Neural Compute"]
        D2 --> M1[PyTorch CUDA Kernels]
        M1 --> M2[YOLOv8 Object Detection]
        M1 --> M3[MONAI Biomedical Segmentation]
        M1 --> M4[Edge Recurrent Classifiers]
    end

    subgraph Optimization["3. Optimization &amp; Quantization"]
        M2 & M3 & M4 --> O1[ONNX Graph Serialization]
        O1 --> O2[TensorRT INT8 / FP16 Engine]
        O2 --> O3[Latency &lt; 15ms Profiling]
    end

    subgraph Serving["4. Edge &amp; Cloud Deployment"]
        O3 --> S1[FastAPI Asynchronous Microservices]
        S1 --> S2[Docker Containerized Mesh]
        S2 --> S3[WhatsApp/SMS Omnichannel Bot]
        S2 --> S4[Autonomous Edge Microcontrollers]
    end

    style Data fill:#161b22,stroke:#58a6ff,stroke-width:1.5px,color:#c9d1d9
    style Modeling fill:#161b22,stroke:#bc8cff,stroke-width:1.5px,color:#c9d1d9
    style Optimization fill:#161b22,stroke:#f0883e,stroke-width:1.5px,color:#c9d1d9
    style Serving fill:#161b22,stroke:#3fb950,stroke-width:1.5px,color:#c9d1d9
```

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## ⏱️ AI &amp; Engineering Activity Metrics

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./hackatime_dark_v1.svg?v=3">
    <img alt="Activity Metrics" src="./hackatime_light_v1.svg?v=3" width="100%">
  </picture>
</div>

<br/>

## 📈 3D Contribution Graph

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-rainbow.svg?v=6">
    <img alt="3D Contribution Graph" src="./profile-3d-contrib/profile-green-animate.svg?v=6" width="100%">
  </picture>
</div>

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## 📊 GitHub Live Analytics

<div align="center">

<table align="center" style="border: none;">
  <tr>
    <td align="center" valign="middle">
      <img src="https://nirzak-streak-stats.vercel.app/?user=livingmangal&theme=tokyonight&hide_border=true&border_radius=10" alt="GitHub Streak" />
    </td>
    <td align="center" valign="middle">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=livingmangal&layout=compact&theme=tokyonight&hide_border=true&border_radius=10" alt="Top Languages" />
    </td>
  </tr>
</table>

</div>

<br/>

## 🐍 Contribution Grid Snake

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/livingmangal/livingmangal/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/livingmangal/livingmangal/output/github-snake.svg">
    <img alt="GitHub Contribution Snake Animation" src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg" width="100%">
  </picture>
</div>

<br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<br/>

## ✍️ Random Dev Quote

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./quote_dark_v1.svg">
    <img alt="Random Dev Quote" src="./quote_light_v1.svg">
  </picture>
</div>

<br/>

## 🤝 Let's Collaborate &amp; Build

<div align="center">

I am always keen to collaborate on forward-thinking research initiatives and high-performance engineering projects:
- 🧠 **Deep Learning Architectures &amp; Distributed Training**
- 👁️ **Computer Vision, Segmentation &amp; Visual Telemetry**
- 🛰️ **Space Tech, Orbital Tracking &amp; Scientific ML**
- ⚡ **Edge AI, TensorRT Ingestion &amp; Low-Latency Inference**
- 🌐 **Scalable Full-Stack Systems &amp; Healthcare AI Engines**

**Open for open-source contributions, research collaborations, and engineering discussions.**

</div>

<br/>

<!-- Profile Views Counter -->
<div align="center">
  <img src="https://komarev.com/ghpvc/?username=livingmangal&label=Terminal%20Visits&color=58a6ff&style=for-the-badge" alt="Profile Views"/>
</div>

<br/>

<!-- Animated Footer Wave Banner -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20,28&height=180&section=footer&text=Thanks%20for%20Exploring!&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=65&desc=Let%27s%20collaborate%20on%20transformative%20AI%20systems%20%E2%AD%90&descSize=16&descAlignY=85" width="100%" alt="Footer Banner" />
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=Driven+by+Curiosity+%7C+Powered+by+PyTorch+%F0%9F%94%A5;If+you+find+my+work+impactful%2C+leave+a+%E2%AD%90;Happy+Engineering!+%F0%9F%9A%80" alt="Footer Typing SVG" />
</div>
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("[OK] Updated README.md")


def main():
    print("Generating assets for livingmangal...")

    # 1. Profile Neofetch SVGs
    with open("dark_mode_v5.svg", "w", encoding="utf-8") as f:
        f.write(build_profile_svg(dark=True))
    with open("light_mode_v5.svg", "w", encoding="utf-8") as f:
        f.write(build_profile_svg(dark=False))
    print("[OK] Created dark_mode_v5.svg and light_mode_v5.svg")

    # 2. Projects SVGs
    with open("projects_dark_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_projects_svg(dark=True))
    with open("projects_light_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_projects_svg(dark=False))
    print("[OK] Created projects_dark_v1.svg and projects_light_v1.svg")

    # 3. Quote SVGs
    with open("quote_dark_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_quote_svg(dark=True))
    with open("quote_light_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_quote_svg(dark=False))
    print("[OK] Created quote_dark_v1.svg and quote_light_v1.svg")

    # 4. Hackatime SVGs
    with open("hackatime_dark_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_hackatime_svg(dark=True))
    with open("hackatime_light_v1.svg", "w", encoding="utf-8") as f:
        f.write(build_hackatime_svg(dark=False))
    print("[OK] Created hackatime_dark_v1.svg and hackatime_light_v1.svg")

    # 5. Build README
    build_readme()

    print("\nAll assets and README generated successfully!")

if __name__ == "__main__":
    main()

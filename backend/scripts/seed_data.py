"""
Database Seeding Script for BhashaSetu
Populates Jharkhand PALASH districts, schools, primary curriculum (Grades 1-5),
vernacular pedagogy entries (Santhali in Ol Chiki, Mundari), and sample users.
"""

import asyncio
from sqlalchemy.future import select
from backend.app.core.database import AsyncSessionLocal, init_db
from backend.app.core.security import get_password_hash
from backend.app.models.user import User, UserRole, District, School
from backend.app.models.curriculum import (
    CurriculumSubject,
    Chapter,
    Concept,
    VernacularConcept,
    MultimodalAsset,
)
from backend.app.models.hitl import ReviewTask, ReviewStatus
from backend.app.services.ai.tts_service import TTSService


async def seed():
    await init_db()
    async with AsyncSessionLocal() as db:
        print("[+] Seeding BhashaSetu Database...")

        # 1. Seed Districts
        districts_data = [
            {"name": "West Singhbhum (Chaibasa)", "is_palash_pilot": True, "primary_tribal_languages": "sat,hoc,unr"},
            {"name": "Khunti", "is_palash_pilot": True, "primary_tribal_languages": "unr,sck"},
            {"name": "Dumka", "is_palash_pilot": True, "primary_tribal_languages": "sat,kht"},
            {"name": "Pakur", "is_palash_pilot": True, "primary_tribal_languages": "sat,kht"},
            {"name": "Gumla", "is_palash_pilot": True, "primary_tribal_languages": "kru,khr,sck"},
            {"name": "Simdega", "is_palash_pilot": True, "primary_tribal_languages": "khr,unr,sck"},
            {"name": "East Singhbhum (Jamshedpur)", "is_palash_pilot": True, "primary_tribal_languages": "sat,hoc,kyw"},
            {"name": "Ranchi", "is_palash_pilot": True, "primary_tribal_languages": "kru,unr,sck,tdb"},
        ]

        district_objs = {}
        for d in districts_data:
            existing = await db.execute(select(District).where(District.name == d["name"]))
            district = existing.scalars().first()
            if not district:
                district = District(**d)
                db.add(district)
                await db.flush()
            district_objs[d["name"]] = district

        # 2. Seed Pilot Schools
        schools_data = [
            {"code": "20200100101", "name": "Govt. Primary School, Chaibasa", "block": "Chaibasa", "district_id": district_objs["West Singhbhum (Chaibasa)"].id},
            {"code": "20200200102", "name": "Utkramit Middle School, Murhu", "block": "Murhu", "district_id": district_objs["Khunti"].id},
            {"code": "20200300103", "name": "Govt. Tribal Ashram School, Dumka", "block": "Dumka", "district_id": district_objs["Dumka"].id},
        ]

        school_objs = {}
        for s in schools_data:
            existing = await db.execute(select(School).where(School.code == s["code"]))
            school = existing.scalars().first()
            if not school:
                school = School(**s)
                db.add(school)
                await db.flush()
            school_objs[s["name"]] = school

        # 3. Seed Users
        users_data = [
            {
                "username": "teacher_santhali",
                "email": "teacher.santhali@jepc.jharkhand.gov.in",
                "full_name": "Birsa Hansda",
                "hashed_password": get_password_hash("teacher123"),
                "role": UserRole.TEACHER,
                "preferred_language": "sat",
                "preferred_script": "olck",
                "grade": 3,
                "school_id": school_objs["Govt. Primary School, Chaibasa"].id,
            },
            {
                "username": "linguist_expert",
                "email": "linguist.reviewer@bhashasetu.org",
                "full_name": "Dr. Nirmala Murmu",
                "hashed_password": get_password_hash("linguist123"),
                "role": UserRole.LINGUIST_REVIEWER,
                "preferred_language": "sat",
                "preferred_script": "olck",
                "school_id": None,
            },
            {
                "username": "admin_jepc",
                "email": "admin@jepc.jharkhand.gov.in",
                "full_name": "JEPC System Administrator",
                "hashed_password": get_password_hash("admin123"),
                "role": UserRole.ADMIN,
                "preferred_language": "hin",
                "preferred_script": "deva",
                "school_id": None,
            }
        ]

        for u in users_data:
            existing = await db.execute(select(User).where(User.username == u["username"]))
            if not existing.scalars().first():
                user = User(**u)
                db.add(user)

        # 4. Seed Curriculum (Grades 1-5 Environmental Studies & Math)
        subject_data = {
            "code": "G3_EVS_JCERT",
            "name": "पर्यावरण अध्ययन (हमारा परिवेश - Aas Paas)",
            "grade": 3,
            "curriculum_source": "JCERT/PALASH"
        }
        existing_subj = await db.execute(select(CurriculumSubject).where(CurriculumSubject.code == subject_data["code"]))
        subject = existing_subj.scalars().first()
        if not subject:
            subject = CurriculumSubject(**subject_data)
            db.add(subject)
            await db.flush()

            # Chapter 1: Our Plants and Trees (हमारे पेड़-पौधे)
            ch1 = Chapter(
                chapter_number=1,
                title="हमारे पेड़-पौधे और जंगल",
                summary="पेड़-पौधों के भाग, सखुआ (साल) के पेड़ और सरहुल पर्व का महत्व।",
                subject_id=subject.id
            )
            db.add(ch1)
            await db.flush()

            # Concept 1: Sal Tree & Lifecycle
            concept1 = Concept(
                title="साल (सखुआ) का पेड़ और उसकी उपयोगिता",
                standard_text_hindi="साल का पेड़ झारखंड के जंगलों का प्रमुख वृक्ष है। सरहुल के त्योहार में साल के फूलों से प्रकृति का पूजन होता है। इसकी पत्तियां और छाया हमें जीवन देती हैं।",
                standard_text_english="The Sal tree is the dominant tree in Jharkhand forests. During Sarhul festival, its blossoms are revered.",
                pedagogy_keywords="sal tree, sarhul, forest, nature, leaves",
                chapter_id=ch1.id
            )
            db.add(concept1)
            await db.flush()

            # Santhali in Ol Chiki Vernacular Concept
            vc_sat = VernacularConcept(
                concept_id=concept1.id,
                language_code="sat",
                script_code="olck",
                simplified_title="ᱥᱟᱨᱡᱚᱢ ᱫᱟᱨᱮ (Sarjom Dare)",
                simplified_explanation="ᱥᱟᱨᱡᱚᱢ ᱫᱟᱨᱮ ᱫᱚ ᱟᱵᱚᱣᱟᱜ ᱵᱤᱨ ᱨᱮᱱᱟᱜ ᱢᱟᱨᱟᱝ ᱫᱟᱨᱮ ᱠᱟᱱᱟ᱾ ᱵᱟᱦᱟ ᱯᱚᱨᱚᱵᱽ ᱨᱮ ᱥᱟᱨᱡᱚᱢ ᱵᱟᱦᱟ ᱛᱮ ᱥᱤᱨᱡᱚᱱ ᱵᱚ ᱥᱮᱵᱟᱭᱟ᱾",
                cultural_metaphor="जैसे बाहा/सरहुल परब में सारजोम (साल) फूल की पूजा होती है, वैसे ही यह पेड़ पूरे जंगल को जीवन देता है।",
                is_verified_by_linguist=1,
                quality_score=5.0
            )
            db.add(vc_sat)
            await db.flush()

            # Audio Multimodal Asset for Santhali Concept
            audio_url, duration, size = TTSService.synthesize_speech(
                text=vc_sat.simplified_explanation,
                language_code="sat",
                script_code="olck"
            )
            audio_asset = MultimodalAsset(
                vernacular_concept_id=vc_sat.id,
                asset_type="AUDIO",
                file_path=audio_url,
                duration_seconds=duration,
                file_size_bytes=size,
                script_content=vc_sat.simplified_explanation
            )
            db.add(audio_asset)

            # Mundari Vernacular Concept
            vc_unr = VernacularConcept(
                concept_id=concept1.id,
                language_code="unr",
                script_code="deva",
                simplified_title="सारजोम दारु (Sarjom Daru)",
                simplified_explanation="सारजोम दारु आबूवाः बीर रेयाः मारंग दारु ताना। बा परब रे सारजोम बा ते आबू सिंगबोंगा के जोहार लेका मनावेया।",
                cultural_metaphor="बा परब (सरहुल) में साल फूल से प्रकृति का जोहार किया जाता है।",
                is_verified_by_linguist=1,
                quality_score=4.9
            )
            db.add(vc_unr)

        # 5. Seed HITL Review Tasks
        hitl_samples = [
            {
                "task_type": "TRANSLATION_VERIFICATION",
                "language_code": "sat",
                "script_code": "olck",
                "source_text": "जल ही जीवन है और हमें पानी बचाना चाहिए।",
                "machine_translation": "ᱫᱟᱜ ᱜᱮ ᱡᱤᱣᱤ ᱠᱟᱱᱟ ᱟᱨ ᱟᱵᱚ ᱫᱟᱜ ᱵᱟᱧᱪᱟᱣ ᱦᱩᱭᱩᱜ-ᱟ᱾",
                "status": ReviewStatus.PENDING,
                "notes": "Awaiting linguist phonetic cadence confirmation."
            },
            {
                "task_type": "SCRIPT_CHECK",
                "language_code": "sat",
                "script_code": "olck",
                "source_text": "गणित में गिनती सीखना",
                "machine_translation": "ᱮᱞᱠᱷᱟ ᱨᱮ ᱞᱮᱠᱷᱟ ᱪᱮᱫᱚᱜ",
                "status": ReviewStatus.APPROVED,
                "accuracy_score": 5.0,
                "cultural_appropriateness_score": 5.0,
                "notes": "Ol Chiki numerals and terminology verified."
            }
        ]

        for task_item in hitl_samples:
            existing_task = await db.execute(
                select(ReviewTask).where(ReviewTask.source_text == task_item["source_text"])
            )
            if not existing_task.scalars().first():
                task = ReviewTask(**task_item)
                db.add(task)

        await db.commit()
        print("[SUCCESS] Seeding completed successfully!")


if __name__ == "__main__":
    asyncio.run(seed())

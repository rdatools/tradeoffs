"""
CONSTANTS

NOTE - This is an updated copy of constants.py from the original PG repo,
  extended for upper & lower state house plans.
"""

from typing import Any, List, Dict

TRADEOFFS_STATES: list[str] = [
    "AL",
    "AZ",
    "CA",
    "CO",
    "FL",
    "GA",
    "IL",
    "IN",
    "MD",
    "MA",
    "MI",
    "MN",
    "MO",
    "NJ",
    "NY",
    "NC",
    "OH",
    "PA",
    "SC",
    "TN",
    "TX",
    "VA",
    "WA",
    "WI",
]  # 24 states with 7 or congressional districts

SAMPLE_STATES: List[str] = ["NC", "PA", "MD", "IL", "SC", "TX"]

# These are the ids for the published official maps in DRA
OFFICIAL_MAPS: Dict[str, Dict[str, str]] = {
    "AL": {
        "congress": "b1cfc3f6-27df-498d-a147-0664d75fea88",
        "lower": "642e8d2a-248c-4191-a88a-a6cdad508cdb",
        "upper": "b694ea80-20d6-45fb-a0e2-09ddaa2880d5",
    },
    "AZ": {
        "congress": "4ee8ecf2-14b7-4a8d-99bc-82fa633a9305",
        "upper": "72e34ca5-9ae1-4ddd-96f0-697bd261294e",
    },
    "AR": {
        "congress": "fa3434ec-4f52-48de-947b-5998b6937bf0",
        "lower": "583730d5-1254-4dca-8f73-850940804307",
        "upper": "083cee53-0d0c-43af-ace1-863ccd3a2fe5",
    },
    "CA": {
        "congress": "fc9d2d06-7c7f-451c-92cb-122127a79c29",
        "lower": "43cea5ab-ef0a-4946-b3e2-c3f2aaf73cf1",
        "upper": "f0a4ed9d-205f-4122-abab-fa3c75b6b050",
    },
    "CO": {
        "congress": "39f44408-23f7-439d-b7eb-923da58b63df",
        "lower": "dee1f8ad-23c1-497b-859c-6d1a9293bbd5",
        "upper": "9b5ec272-1fba-4a7a-ac6c-f2dcb4c6d0ae",
    },
    "CT": {
        "congress": "707f203c-ce98-4de8-b150-a2605136e015",
        "lower": "2e38109d-9987-46e3-9ff0-dd6c3caa59e8",
        "upper": "fc9e83c0-59e2-4dea-b0cf-d2fff1c0b8a3",
    },
    "FL": {
        "congress": "3a6791b9-a186-4691-a95c-5d51dbb3be1c",
        "lower": "488c9284-a2c4-4846-9d7d-08af9d98a6c5",
        "upper": "91f2ce50-b3c1-4d74-87f2-d3a9fa078129",
    },
    "GA": {
        "congress": "3a370cc7-f820-4af4-8fca-a27ec52502b7",
        "lower": "041f73c7-8f4f-48c5-a5ff-cb059e692827",
        "upper": "f1249844-4b84-45e6-9ca6-e13f6ddddb0d",
    },
    "ID": {
        "congress": "ebc8cec8-b919-4a66-9b42-9cf5bf7e02a1",
        "upper": "a56da372-79a4-48e7-9fd5-b689d0ccb602",
    },
    "IL": {
        "congress": "8a4586ad-4c58-489b-828c-4477cfd0ce88",
        "lower": "19bc2a13-2ad1-455a-a7cb-4182ff7c6f6f",
        "upper": "8cd5c7ba-6e69-42a7-89e1-3806a2a05e64",
    },
    "IN": {
        "congress": "c08c9df0-9756-4c5a-a7e7-01ff03bbb170",
        "lower": "db849782-86e9-4293-a492-3e17d7cfceab",
        "upper": "f2d2e4a3-f50d-4f77-bc5d-027ba0e2717e",
    },
    "IA": {
        "congress": "628d5e9a-bd35-4248-aa8c-73af095e0135",
        "lower": "3bba1647-f4a4-4374-8021-a8e4aeb6f15a",
        "upper": "0e81cf3d-648d-4851-b14b-0ee893f92610",
    },
    "KS": {
        "congress": "2ea884cd-5687-48b4-879a-4f780d3de1cf",
        "lower": "781f29f1-259e-4235-8b14-85137bc38893",
        "upper": "2bc2f97f-a285-4596-9fcd-6108056b229f",
    },
    "KY": {
        "congress": "0ec1616e-7ed6-4f84-b20d-dcc51221b2bf",
        "lower": "8eed4db7-46cd-4e09-a179-c0a7e821a963",
        "upper": "8ef6d39b-ae52-4587-8ed1-88b781dd4300",
    },
    "LA": {
        "congress": "42873bd9-ce68-4ee1-878e-be420dbf0ee3",
        "lower": "d63b737c-a8b3-46e9-8855-aa20a728c2b5",
        "upper": "12eedba5-68de-4ab4-a3bb-7f59d9268041",
    },
    "MA": {
        "congress": "791f8174-e00d-4baf-9b0a-206a298eb28b",
        "lower": "f4bfa2f3-1e73-4e0b-a237-cc2aa2e611b8",
        "upper": "b32decd8-3ed9-4ab2-876b-c92cfa798e33",
    },
    "MD": {
        "congress": "a365ecbd-db5f-4c84-a77f-90310c6a6c1a",
        "lower": "4cf1f21b-2347-457a-bbca-f299c7a8cb2b",
        "upper": "92ad6e43-2394-4957-b30a-828ca424a034",
    },
    "MI": {
        "congress": "287ace43-1a66-4686-b596-949f578971a8",
        "lower": "8f2d562d-9d7f-4d3b-992e-5c52debd8f08",
        "upper": "7563fcf7-de01-411a-aa51-c56cf76340b0",
    },
    "MN": {
        "congress": "4b212b88-2b8b-48aa-b2d2-e2f9980ac884",
        "lower": "0e589052-0df8-4b8a-bede-c8e9fcc8814c",
        "upper": "8d55ed9f-d825-4a8a-95e4-864cbeede612",
    },
    "MS": {
        "congress": "2a63d0b3-58db-4e59-9b3b-436b221e078a",
        "lower": "f8554517-7286-461a-9cfa-892b3d4731f7",
        "upper": "f3908ec6-949f-444b-9fd5-7b2173abcb6e",
    },
    "MO": {
        "congress": "68b2b598-69cd-430e-bee2-1dc4b76705f6",
        "lower": "ebb632d0-2569-4a2a-81f6-1d8d6adc0d5e",
        "upper": "8d25c96a-2a78-40b2-b2f0-c504ecaa6762",
    },
    "MT": {
        "congress": "66ff2b64-826d-48a9-bbe4-08afa4c10873",
        "lower": "fe2f2ff5-f70e-459d-8a1f-48b3786c8e64",
        "upper": "0312ecba-7989-480c-bed4-777e2e06c178",
    },
    "NE": {
        "congress": "9de1188c-2169-4c5a-a4f3-76179d22b279",
        "upper": "ab1f2fef-b979-4431-844a-98d93a4d6730",
    },
    "NH": {
        "congress": "a1a2b285-f862-402c-9e89-b45791a46473",
        "lower": "dfddaed1-5a76-4ca7-8a11-ddc533ea9f6e",
        "upper": "15bf8903-0c56-4536-9265-7b7177726a73",
    },
    "NV": {
        "congress": "eb89e40d-595f-485f-9a43-d1bbdd6d0cb4",
        "lower": "2a33203f-8725-48dc-ba1b-478bd6012a58",
        "upper": "99808524-5012-4119-91ce-973ba647806b",
    },
    "NJ": {
        "congress": "6ff0b024-2e5d-4e9b-ba0e-56f6de17ea80",
        "upper": "61388384-5d1f-4f3b-9669-31e485b781f1",
    },
    "NM": {
        "congress": "ec1c76cd-f59f-445b-8f24-fbffb0e8bdf5",
        "lower": "5e00bd63-7008-4b5e-b570-db5ba1d36785",
        "upper": "11c9cc63-8521-4785-89f3-58b5e4359507",
    },
    "NY": {
        "congress": "395a7fbe-fa32-47fc-993d-e07d36baff72",
        "lower": "1933abca-db19-40f9-808d-17dd90642cdc",
        "upper": "bb78268d-ea3c-46a1-a484-c192a6c0e15d",
    },
    "NC": {
        "congress": "6e8268a4-3b9b-4140-8f99-e3544a2f0816",
        "lower": "e4b677ba-541f-40bd-ad9f-ba8707515f7d",
        "upper": "8288b613-df48-45a7-9bd1-5d9f9ca3d685",
    },
    "OH": {
        "congress": "64d56870-70ea-4f4d-b667-9a4fd60ac511",
        "lower": "90de759b-f81d-44c0-a019-d2714a38cc3a",
        "upper": "6eba71b1-18a1-48d1-99c9-62afba432253",
    },
    "OK": {
        "congress": "f726bcb3-b750-44b2-9d0b-e2df90fe6fa5",
        "lower": "a4a178b9-581b-4591-bcf9-13e18bd850ea",
        "upper": "0fa6fe25-9db7-4777-a150-d2309188823f",
    },
    "OR": {
        "congress": "9b2b545f-5cd2-4e0d-a9b9-cc3915a4750f",
        "lower": "c572dfa0-276b-4a76-8531-06669d885f27",
        "upper": "a5aadfab-0234-489a-a4df-cc008a844926",
    },
    "PA": {
        "congress": "b0a94d77-5d99-41c5-bc01-5859a6e1f3e6",
        "lower": "12a18072-adf1-48ac-a9d1-12280567b824",
        "upper": "317011f0-6bcd-4df6-a1ee-435a92640426",
    },
    "RI": {
        "congress": "cffbb279-824c-47b8-90c7-3070378e37ae",
        "lower": "90ec6599-f715-4a3a-b50b-5858788046ac",
        "upper": "2aab93a2-7e15-4047-87a8-02b0deb3eb4e",
    },
    "SC": {
        "congress": "839561a1-8c15-4c4b-ab56-3275d68092f9",
        "upper": "7c9df455-6865-4f9e-8172-7c1a26ab28b9",
        "lower": "f886f454-bdf5-463e-823e-7dfe56c8bbdd",
    },
    "TN": {
        "congress": "445d4976-c994-473f-b14c-4b87464b07ee",
        "lower": "c0ed8258-ce44-4eec-9736-2cc3b86a9d16",
        "upper": "62c62bed-a104-4afc-9286-9b3915b45f58",
    },
    "TX": {
        "congress": "1c2c1e0d-2fd1-43a8-a039-73e7023124d1",
        "lower": "e74af879-6ba8-4a5c-b946-0b9364aae40b",
        "upper": "94b33bee-887d-4170-b154-80aa55c8fe5b",
    },
    "UT": {
        "congress": "b4d46a7e-4366-4f6c-ac54-ff6640d4e13f",
        "lower": "927e8547-08f9-43e3-8abc-68a7faf89d71",
        "upper": "cfd457c9-6d3e-496d-9377-4b68de384a57",
    },
    "VA": {
        "congress": "bc930c25-236f-46a7-bbe9-d8d77e21d011",
        "lower": "fa427b6b-e057-43e9-8000-9d1ae319870e",
        "upper": "1b489a5a-f457-428d-b552-9ede8ceb9b99",
    },
    "WA": {
        "congress": "3dd8f07d-8f9b-4905-a155-573bdc084b06",
        "upper": "3e3c5f5c-3a83-4847-b1d8-5328fb3b9e31",
    },
    "WI": {
        "congress": "aa64c8f5-837c-474f-819f-6eaa1094d776",
        "lower": "6a8a362d-0c59-4d81-aea3-28cba004b502",
        "upper": "cb8ed0b5-013f-4b1a-ba49-1b03445416c9",
    },
    "WV": {
        "congress": "aaaa571f-f204-4cbe-bcf1-404db0519d36",
        "lower": "bd6eb9ac-ac94-465f-82d6-4e086307d5e5",
        "upper": "c3ca956f-0b1d-4750-894d-b2e9dadc642c",
    },
}  # This was autogenerated from state_plans.json using the make_official_ids_dict.py script

# These are the ids for *copies* of the published official maps in DRA,
# duplicated on 09-24-24.
OFFICIAL_MAPS_COPY: Dict[str, Dict[str, str]] = {
    "AL": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "b6ab3795-3322-4fad-bcfd-a5699571dd78",
        "upper": "3e2c7de9-5fbd-480a-8e71-ad9d0a0cb383",
    },
    "AZ": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "upper": "6b1bb5e2-5478-40da-8987-b38fefa10970",
    },
    "AR": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "6da596db-f412-401f-aa78-22d51aebce0d",
        "upper": "c24abde6-7638-40f7-8c88-b85e65f68147",
    },
    "CA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "8e557c04-ed26-49ca-887d-b4334820a9c1",
        "upper": "9a0d377b-227d-4e1a-9e20-cecb01ef5e72",
    },
    "CO": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "47712e51-4c95-40a9-a118-e51cc6ec626d",
        "upper": "e89181c3-998a-41c0-8c73-735ff6b3f9cd",
    },
    "CT": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "5578f5df-2bf9-48a2-b7b5-1fdbd1ca2ae0",
        "upper": "af21d400-9673-4c07-8db7-849b09978a59",
    },
    "FL": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "6a228d09-a065-4c5b-afbf-93ce6e02a8e9",
        "upper": "90397d77-9d79-4fa2-bc3f-0c74fad61e2f",
    },
    "GA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "ca21b753-93fb-462a-9f7c-ecf3f1472699",
        "upper": "2793817d-15b2-4bc9-a335-38ad5afeaca0",
    },
    "ID": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "upper": "9c6bc760-84d6-4309-8c1c-706da33a0227",
    },
    "IL": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "22ab887c-ad8d-4605-8979-37640135bb7b",
        "upper": "123fc62b-531a-42ce-8ac3-8b5dc689f45c",
    },
    "IN": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "2af05eb4-3d18-4fd3-b392-080bd082e085",
        "upper": "a54fce0c-506c-41e4-8260-6b1f677c4caf",
    },
    "IA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "dac9d22d-10ec-4bd7-9334-96297cde2c30",
        "upper": "5f130eb4-c754-4a4c-91b6-48e10fd58197",
    },
    "KS": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "a2a9bfee-bc1b-4e3e-9adf-12c4ea700e1b",
        "upper": "94b7149c-46e2-4d5c-a937-8ca0b905ab45",
    },
    "KY": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "73f1defe-58cc-4abb-97c5-99f38340c25d",
        "upper": "d64c54ca-418b-470f-8431-921e768854cd",
    },
    "LA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "46ca79be-18a2-4721-a872-cdb09c412731",
        "upper": "9cf956da-b467-4484-97ab-be7696fd37f0",
    },
    "MA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "0fa95b32-fe01-4f5f-b94c-b0e0351b3b38",
        "upper": "6383f0e3-5110-4451-a8db-d5ff0f511c73",
    },
    "MD": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        # "lower": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", N/A - uses MMD
        "upper": "3343ba77-9704-4433-84b2-e01b8f7bfeed",
    },
    "MI": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "3f8db2b5-b120-4804-b35b-d003f79f913d",
        "upper": "f0f8da97-55e3-4655-9cce-806c8475a0ab",
    },
    "MN": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "f7b603fa-50a2-4095-9ee0-b70250742741",
        "upper": "6cec1ccd-844f-4f2c-a230-b616018bde82",
    },
    "MS": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "56463bff-513c-467c-94bf-9d5a7376938f",
        "upper": "a1b980a1-2bcf-4f30-a310-6a9e51836f3e",
    },
    "MO": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "96dd2fad-178d-40f3-a584-508c10b467bf",
        "upper": "53a1b0b0-7bab-42e0-8d65-e5846e764fe4",
    },
    "MT": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "3f1ed6e0-14c7-4cdf-9f7b-bd6f4e2c7498",
        "upper": "cf72bdfa-6e0f-4dc7-b386-4b3097c76584",
    },
    "NE": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "upper": "7dd74598-1af0-4684-853e-7797909f9749",
    },
    "NH": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
        "upper": "b25c34ca-5543-44ed-8a97-6d2541bca807",
    },
    "NV": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "05fe1b84-6426-4185-b052-ab747c10e240",
        "upper": "2dc66a7c-b659-439f-ba2e-ba7cc1961473",
    },
    "NJ": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "upper": "cdbc6fca-09e1-4aba-b873-5c47288180d4",
    },
    "NM": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "34f34ce1-9afd-4025-baac-03e4d78cfd0c",
        "upper": "477c4620-fc8f-4b5a-8d7a-4e8a3050f5ff",
    },
    "NY": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "e830d88b-d2e5-4b65-9267-b815f4743c5e",
        "upper": "5f2ed9da-19db-4c73-a3f1-329ff9017cf7",
    },
    "NC": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "474791f9-6452-4be3-8dcd-a45d104dbbee",
        "upper": "bf272ccb-7218-4517-ab04-c7fafcfc0504",
    },
    "OH": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "9a7f07a6-fdda-46e1-822f-e51238705e14",
        "upper": "abdfa849-d406-4070-a306-93efb432b833",
    },
    "OK": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "4185e575-666b-47cf-be6a-6d9585247649",
        "upper": "a7e29d0b-84b7-41e2-9f7a-ba99241151e9",
    },
    "OR": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "eedb122b-7d89-48f6-b405-d35e11e85327",
        "upper": "a64b165c-48c8-493b-aada-cd4cc4ad58a4",
    },
    "PA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "6be1787a-5229-4f2f-af06-9f808027126d",
        "upper": "69db0612-e79b-4772-a2b8-ee7f67b9437d",
    },
    "RI": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
        "upper": "c067a443-87ba-488f-8017-ced48d9bff29",
    },
    "SC": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "3bcc81b5-c145-4783-8de4-dee5af5bb5fc",
        "upper": "9b61d588-fda5-4973-bb90-a535a7067173",
    },
    "TN": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "93719c9e-02bc-4e29-bce1-fcfdcbc54062",
        "upper": "0a314504-9b61-479a-ae6a-701ca2c2dfc8",
    },
    "TX": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "6d85995d-d5cd-48d5-96a4-ea0ac3cf554d",
        "upper": "933b0acb-bba6-4c3c-9652-a5f70631d999",
    },
    "UT": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "e748c2ea-105a-4744-bedb-92b19725cca4",
        "upper": "6f18a4ad-7677-4d09-b17e-d0f8f5465508",
    },
    "VA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "43a3f59f-f260-4f92-bff0-dd9a5e964485",
        "upper": "6e05c843-7821-4d0f-aba7-5675f5d7e466",
    },
    "WA": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "upper": "76eec368-9ed1-4d0e-af24-31e3fce39473",
    },
    "WI": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "cf18bd70-41bf-4c5a-a1e7-978dfdd6798d",
        "upper": "cb8ed0b5-013f-4b1a-ba49-1b03445416c9",
    },
    "WV": {
        "congress": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "lower": "e4598f7f-1e56-43b2-b696-7e585f07ec83",
        "upper": "53904ef8-a72c-4a5d-9a05-8f321e837834",
    },
}

"""
These are the ids for notable maps in DRA.
NOTE - They may not be the *actual* notable maps, we they were derived by analyzing
a dump of the DRA database and finding the best plans on each dimension.

These state / plan type / dimension combos had no leaders. I substituted the official
maps instead.

{'xx': 'ID', 'plan_type': 'congress', 'dimension': 'proportionality'}
{'xx': 'ID', 'plan_type': 'congress', 'dimension': 'competitiveness'}
{'xx': 'ID', 'plan_type': 'congress', 'dimension': 'minority'}
{'xx': 'ID', 'plan_type': 'congress', 'dimension': 'compactness'}
{'xx': 'ID', 'plan_type': 'congress', 'dimension': 'splitting'}
{'xx': 'NH', 'plan_type': 'congress', 'dimension': 'proportionality'}
{'xx': 'NH', 'plan_type': 'congress', 'dimension': 'competitiveness'}
{'xx': 'NH', 'plan_type': 'congress', 'dimension': 'minority'}
{'xx': 'NH', 'plan_type': 'congress', 'dimension': 'compactness'}
{'xx': 'NH', 'plan_type': 'congress', 'dimension': 'splitting'}
{'xx': 'NH', 'plan_type': 'lower', 'dimension': 'proportionality'}
{'xx': 'NH', 'plan_type': 'lower', 'dimension': 'competitiveness'}
{'xx': 'NH', 'plan_type': 'lower', 'dimension': 'minority'}
{'xx': 'NH', 'plan_type': 'lower', 'dimension': 'compactness'}
{'xx': 'NH', 'plan_type': 'lower', 'dimension': 'splitting'}
{'xx': 'RI', 'plan_type': 'congress', 'dimension': 'proportionality'}
{'xx': 'RI', 'plan_type': 'congress', 'dimension': 'competitiveness'}
{'xx': 'RI', 'plan_type': 'congress', 'dimension': 'minority'}
{'xx': 'RI', 'plan_type': 'congress', 'dimension': 'compactness'}
{'xx': 'RI', 'plan_type': 'congress', 'dimension': 'splitting'}
{'xx': 'RI', 'plan_type': 'upper', 'dimension': 'proportionality'}
{'xx': 'RI', 'plan_type': 'upper', 'dimension': 'competitiveness'}
{'xx': 'RI', 'plan_type': 'upper', 'dimension': 'minority'}
{'xx': 'RI', 'plan_type': 'upper', 'dimension': 'compactness'}
{'xx': 'RI', 'plan_type': 'upper', 'dimension': 'splitting'}
{'xx': 'RI', 'plan_type': 'lower', 'dimension': 'proportionality'}
{'xx': 'RI', 'plan_type': 'lower', 'dimension': 'competitiveness'}
{'xx': 'RI', 'plan_type': 'lower', 'dimension': 'minority'}
{'xx': 'RI', 'plan_type': 'lower', 'dimension': 'compactness'}
{'xx': 'RI', 'plan_type': 'lower', 'dimension': 'splitting'}
{'xx': 'WV', 'plan_type': 'congress', 'dimension': 'proportionality'}
{'xx': 'WV', 'plan_type': 'congress', 'dimension': 'competitiveness'}
{'xx': 'WV', 'plan_type': 'congress', 'dimension': 'minority'}
{'xx': 'WV', 'plan_type': 'congress', 'dimension': 'compactness'}
{'xx': 'WV', 'plan_type': 'congress', 'dimension': 'splitting'}
"""
NOTABLE_MAPS: Dict[str, Dict[str, Dict[str, str]]] = {
    "AL": {
        "congress": {
            "proportionality": "93441051-8abb-4543-845a-3787100bcedd",
            "competitiveness": "04301958-88ca-454d-8cba-a68c44278528",
            "minority": "93441051-8abb-4543-845a-3787100bcedd",
            "compactness": "9a0a4eb9-8be2-4166-a58c-3df2847b9a52",
            "splitting": "13df03d7-87b3-40ca-820a-4e994d902b50",
        },
        "upper": {
            "proportionality": "f8bccaba-5062-4dab-8139-18ae5f908ac4",
            "competitiveness": "a80e8693-853e-4859-8b24-9d2306ccf008",
            "minority": "3e75f081-860d-47ba-98cd-12388a003589",
            "compactness": "a9b3edb6-8377-4d52-adea-23eefd16f5ce",
            "splitting": "4049d60e-bfd4-454e-8b7b-a3f77c6a82b3",
        },
        "lower": {
            "proportionality": "bdd19ed2-64df-49e4-9c0a-fb88a278dd2b",
            "competitiveness": "2b570021-0d81-47cb-94d5-b23a5753a8b7",
            "minority": "f557be18-69a0-4270-9b70-8830cbc51d1a",
            "compactness": "e7ef57c3-2033-4606-8f9e-72bfddf28dd3",
            "splitting": "e7ef57c3-2033-4606-8f9e-72bfddf28dd3",
        },
    },
    "AK": {
        "upper": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "lower": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
    },
    "AZ": {
        "congress": {
            "proportionality": "8f1dac18-9258-4822-ae51-cebf704e8e1f",
            "competitiveness": "8f1dac18-9258-4822-ae51-cebf704e8e1f",
            "minority": "7e74835b-b049-4358-a4f8-5f25ebcbf550",
            "compactness": "8f1dac18-9258-4822-ae51-cebf704e8e1f",
            "splitting": "1998970d-404e-4f14-ba78-1f932a01127f",
        },
        "upper": {
            "proportionality": "1254a0e8-ac71-4ac8-b1e4-ce5c971ea3a7",
            "competitiveness": "f74c2589-caab-407f-95e3-972b98da6b0a",
            "minority": "00cf1114-746b-421a-94a8-0e6451458228",
            "compactness": "3c1194c1-2bc3-4cee-83c6-8555ef737052",
            "splitting": "1254a0e8-ac71-4ac8-b1e4-ce5c971ea3a7",
        },
    },
    "AR": {
        "congress": {
            "proportionality": "c0b88657-2373-438e-9d1e-ce0e7a5895f2",
            "competitiveness": "05a6a949-c4e6-4126-884c-d248a4ba96c2",
            "minority": "b94e655e-c896-41af-a6a9-44b607674dd0",
            "compactness": "8bd966ed-b68c-417b-b594-0561aaada1c7",
            "splitting": "e9cd20ac-03d1-4c02-996d-c204cb79dd46",
        },
        "upper": {
            "proportionality": "2a4f87d9-f02e-4b47-a7be-878e60a2297e",
            "competitiveness": "9077271d-53a6-45ba-a3af-f2cd897346e5",
            "minority": "3e476bb0-7723-41ff-bf32-d0a3fc6f55bf",
            "compactness": "5d6cc220-daaf-4c67-95a2-12c115229a54",
            "splitting": "02ad985b-0e89-4afd-b568-7649cc185043",
        },
        "lower": {
            "proportionality": "deacabbd-0113-4275-8297-52b45c6d384c",
            "competitiveness": "29e78512-ae7d-4649-9bb0-8c295d45f24a",
            "minority": "b79c23c1-e6ea-4589-a9a2-5533e585d3bb",
            "compactness": "deacabbd-0113-4275-8297-52b45c6d384c",
            "splitting": "deacabbd-0113-4275-8297-52b45c6d384c",
        },
    },
    "CA": {
        "congress": {
            "proportionality": "f5bc18d0-6d4b-40c1-91bb-7fe044e04b62",
            "competitiveness": "7c0b3d88-0267-43bb-a873-fa4c63d425c1",
            "minority": "b79d4e43-2fc4-42cd-8370-de163c320368",
            "compactness": "e20051ec-1544-4f3a-9688-c4d9e986649c",
            "splitting": "774a680c-ad29-43d5-af16-6b9c6cc2f17f",
        },
        "upper": {
            "proportionality": "3e494a38-690e-4413-8f73-5687f14eeb4c",
            "competitiveness": "79d5ca6e-2330-4122-a455-76c9f079f401",
            "minority": "3fbd08e0-b879-4b12-aa36-9a1cfe9bf944",
            "compactness": "64a1db24-e180-4c7a-821c-2e4920c80e50",
            "splitting": "9f11cd00-fce8-4824-be47-a8a671ff802a",
        },
        "lower": {
            "proportionality": "467f046b-6608-47cd-b3af-4b7b98cfe661",
            "competitiveness": "78ce7f51-427c-4181-9aaf-24e291779e5a",
            "minority": "9cec0d38-dd51-405d-a72f-58bbb657de46",
            "compactness": "467f046b-6608-47cd-b3af-4b7b98cfe661",
            "splitting": "13d959fb-d09d-4bdc-b7a7-5c02c0400080",
        },
    },
    "CO": {
        "congress": {
            "proportionality": "3a6dbd88-e1fa-4c20-8b38-13da468ff32a",
            "competitiveness": "6f696afa-73e7-4ff4-8407-c4386d65ebd2",
            "minority": "fd8ff456-b8c6-437d-98d9-70e560a3ac30",
            "compactness": "af01f470-753a-4247-862f-eeeb12604ec7",
            "splitting": "a78ca039-b9af-4816-ae03-6f842f3cab9c",
        },
        "upper": {
            "proportionality": "374c6b38-662c-4625-b2d3-4c0188a3d3f9",
            "competitiveness": "ac0b0d5e-4fae-4d83-a33f-be580802adf3",
            "minority": "d6484a40-0804-46d7-bc25-228acc57509c",
            "compactness": "3e3ecf92-2ae1-4cf2-8b8d-741b7231a166",
            "splitting": "f0babbbc-980c-4bd9-a974-e3947c778270",
        },
        "lower": {
            "proportionality": "c6d723af-62d0-44e4-9df4-316fc825ab1c",
            "competitiveness": "dd15c6e4-d37c-4440-9dad-44ed44ea1693",
            "minority": "e13c971e-44c4-4899-86a1-29236475aeb1",
            "compactness": "3417e69c-94db-4e4b-8cad-7ff51748b557",
            "splitting": "fe79f9f1-7f75-4b5f-8289-78102be08359",
        },
    },
    "CT": {
        "congress": {
            "proportionality": "57d517f0-15ea-476b-866a-172e1e96144a",
            "competitiveness": "03342fe2-15f8-4f76-b4d4-577dc950c444",
            "minority": "6fcdea1b-57d3-44db-84f0-e074b1aade56",
            "compactness": "6fcdea1b-57d3-44db-84f0-e074b1aade56",
            "splitting": "e0cd942f-ee7f-40c0-a641-50ba23e08989",
        },
        "upper": {
            "proportionality": "585756dd-a555-47da-ad85-7d80d469421e",
            "competitiveness": "6e40328b-4ad3-4244-8fa7-d04a6e9a9bef",
            "minority": "f0e2eded-945a-41a8-b26d-c3dcb5babb74",
            "compactness": "2c550925-4869-4114-badc-ec63d20af223",
            "splitting": "8e88b9fe-038f-4a4c-aa3f-befd3231fa97",
        },
        "lower": {
            "proportionality": "50e244c0-b64e-4555-869d-3afe3fb9176e",
            "competitiveness": "50e244c0-b64e-4555-869d-3afe3fb9176e",
            "minority": "52327cf9-bc38-40ed-9043-1fc3d981c153",
            "compactness": "39da37e1-f965-4f8e-ba4d-9aa9e522e6ad",
            "splitting": "3054b7e0-be13-478c-865b-95c129799892",
        },
    },
    "DE": {
        "upper": {
            "proportionality": "475e9211-0554-467b-bdeb-24eeb671079d",
            "competitiveness": "f6598b17-a996-4beb-9083-195cee3450cb",
            "minority": "16eaaa8f-57b3-4388-b982-01d00862265e",
            "compactness": "7f85825f-497e-4c25-be8e-a65ea43c2eed",
            "splitting": "475e9211-0554-467b-bdeb-24eeb671079d",
        },
        "lower": {
            "proportionality": "22e28e13-395a-43a8-a5a2-32f3db42cf67",
            "competitiveness": "01acfbbc-11d5-44aa-a355-6c7d0d8df5e5",
            "minority": "003d3f2f-d2d1-4dc9-a444-1ef90a508364",
            "compactness": "781a59e1-a97e-4cf8-9f92-83ab57ac2b2a",
            "splitting": "22e28e13-395a-43a8-a5a2-32f3db42cf67",
        },
    },
    "FL": {
        "congress": {
            "proportionality": "a1536c66-e14c-474d-b8bc-be32a61951dc",
            "competitiveness": "d0443475-fd02-4351-a432-d2f529e82da0",
            "minority": "f37f9f03-ba41-49f9-aaf0-196c5b76fa6a",
            "compactness": "a1536c66-e14c-474d-b8bc-be32a61951dc",
            "splitting": "e402f1f6-ec7c-4134-9756-70c2752a914c",
        },
        "upper": {
            "proportionality": "93cbad1e-07d3-4a65-bb9b-ca21aed6a416",
            "competitiveness": "8052f5d6-fc6c-46cd-8d56-acae1054e7ba",
            "minority": "5c730fa1-183f-4bd0-8190-888badcb0ea4",
            "compactness": "5f33299b-72a0-4f2c-a568-4acd7c68f4b9",
            "splitting": "e6b3e3db-aa17-49da-a4fe-5a34d102fcfe",
        },
        "lower": {
            "proportionality": "1a6756f1-c6b1-446c-a778-b803e3fb39e9",
            "competitiveness": "ba64af28-e7dc-4042-b01a-1c424277c627",
            "minority": "e0b94223-4c33-4e66-9162-c585d88222a7",
            "compactness": "e9bc053e-a102-4b52-b133-6731761fcba8",
            "splitting": "1a6756f1-c6b1-446c-a778-b803e3fb39e9",
        },
    },
    "GA": {
        "congress": {
            "proportionality": "0b838758-9127-46cc-9211-c18a3273167c",
            "competitiveness": "e5987b6d-b258-4747-97c6-f7ef0ff0119b",
            "minority": "0b838758-9127-46cc-9211-c18a3273167c",
            "compactness": "16cf555f-e5f0-4dab-b039-e4cb4e0dbd36",
            "splitting": "fadc76f8-d1de-442a-89be-ae4910f3d883",
        },
        "upper": {
            "proportionality": "96df7667-e4bf-41e8-8bbf-13f2369bbd84",
            "competitiveness": "f8ed1a95-e984-4ff8-a839-fc57b3290353",
            "minority": "f4014bf5-808a-4700-ab47-a8566655bbcb",
            "compactness": "a64ab7eb-0f65-40fd-abb7-82e673e37226",
            "splitting": "cd38b7e8-bfb6-4e35-a98c-cfc8f33a3904",
        },
        "lower": {
            "proportionality": "fa153f47-51d1-4275-b1ad-78fd4e36beff",
            "competitiveness": "ce21bcaa-9232-47d8-8d97-25a3df3664a3",
            "minority": "9f5a5c01-dde6-4949-8888-7a14b02fd12e",
            "compactness": "c07acd22-e650-45d7-a24f-eb0a5f6f6461",
            "splitting": "fa153f47-51d1-4275-b1ad-78fd4e36beff",
        },
    },
    "HI": {
        "congress": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "upper": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "lower": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
    },
    "ID": {
        "congress": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "upper": {
            "proportionality": "641f2807-cc5c-421e-8d8d-50636ec62e6e",
            "competitiveness": "f29c5d82-51b1-4e6b-9c9c-145990a15322",
            "minority": "00382389-d0c1-421e-b54b-0968e5db11c4",
            "compactness": "b3c63335-6bb8-4342-a337-303ad83cf23c",
            "splitting": "ea479645-7f55-492e-bdb6-10bd5249fe7a",
        },
    },
    "IL": {
        "congress": {
            "proportionality": "cbad09de-f1de-49da-95ff-1a6553d3d0e3",
            "competitiveness": "e61092ca-cf14-41e6-916e-20fd57c9b248",
            "minority": "60b544e7-41dc-43b8-9d51-969f1aa8b070",
            "compactness": "62003e0b-1485-40b9-aa36-e40acae72757",
            "splitting": "5d70464b-e9fe-420f-95e2-0ecd5ae37fd0",
        },
        "upper": {
            "proportionality": "32120c5a-40e2-47f4-b451-bfe8194ab7b8",
            "competitiveness": "cfe88a7c-2624-488d-bb1f-35ef542c90dc",
            "minority": "0e5e321a-e006-451f-a910-9d71a62f3ee9",
            "compactness": "71d71048-4303-4a11-b2f9-6af3c14e511a",
            "splitting": "32120c5a-40e2-47f4-b451-bfe8194ab7b8",
        },
        "lower": {
            "proportionality": "31821f78-11bc-4917-a337-ab90480cc518",
            "competitiveness": "c352261c-6a31-43ce-b182-1b479f4c0116",
            "minority": "4f41540c-7433-4dea-bf6c-997ff2eb496d",
            "compactness": "1814a00e-b52e-4e9b-a34d-54e052127ac5",
            "splitting": "31821f78-11bc-4917-a337-ab90480cc518",
        },
    },
    "IN": {
        "congress": {
            "proportionality": "c3ef78cf-532d-4c55-8a78-4f2fde608b6a",
            "competitiveness": "ed8c688f-1be2-49a8-ad76-c9e2a951c153",
            "minority": "8bab38bd-cacb-4c6f-8dd2-21d359053176",
            "compactness": "b80fc5ee-4642-4bd0-b60c-a3f0c485d765",
            "splitting": "9e274ebc-4382-4da8-9d22-439ef421e7e5",
        },
        "upper": {
            "proportionality": "77594746-289b-47b1-8f2a-5da85f50809c",
            "competitiveness": "f03800e2-51ce-4fd6-9c15-2160b1399af5",
            "minority": "3beb9712-3bfc-485d-8e1d-68cd4c7d1328",
            "compactness": "83179726-fdf2-44d5-863b-1ed49636fc37",
            "splitting": "0e132f8c-352a-4bea-932b-c0b031f60440",
        },
        "lower": {
            "proportionality": "4095bd84-8265-41b1-8ac9-a1c583b46185",
            "competitiveness": "3dd8b3aa-646c-4561-b4f0-75b1945bf727",
            "minority": "4cc679ff-90f1-4ae2-8e80-a17b46e836eb",
            "compactness": "83463cdd-496f-4a03-b916-85d7578c2566",
            "splitting": "4095bd84-8265-41b1-8ac9-a1c583b46185",
        },
    },
    "IA": {
        "congress": {
            "proportionality": "0b89789e-96e4-4d59-af19-68e4fe33d463",
            "competitiveness": "35a33bd9-685f-49be-b0bd-49e7274a0aa9",
            "minority": "d8b1efb6-089b-4059-bbd7-44d6cb4ad3e0",
            "compactness": "48290d57-3fba-457b-915c-c1648715ddcf",
            "splitting": "605e2dde-819e-4510-82da-8b53da91827b",
        },
        "upper": {
            "proportionality": "4ffd2b97-0964-4764-9160-08046978351c",
            "competitiveness": "27412b9b-249f-4d30-a446-31bc9ed148c2",
            "minority": "27412b9b-249f-4d30-a446-31bc9ed148c2",
            "compactness": "ee7fe64a-fadd-4597-864d-c4863271267a",
            "splitting": "75bf71a3-caef-4bd4-916e-5a87edc940e6",
        },
        "lower": {
            "proportionality": "4b1a4eaf-60bf-4602-a629-b68cf697c6f7",
            "competitiveness": "146acee9-8bf5-48c2-8207-aa64f68d54ed",
            "minority": "54598c0d-e46f-4731-9171-8838ae6efbf5",
            "compactness": "a6a4a14f-87b4-450d-8dd0-134fde5f8fc7",
            "splitting": "4b1a4eaf-60bf-4602-a629-b68cf697c6f7",
        },
    },
    "KS": {
        "congress": {
            "proportionality": "307084a5-8348-444c-9b28-efb9cbc3a0ef",
            "competitiveness": "90843627-6d74-4c24-8d1f-1ec84a304e1b",
            "minority": "2b1ad46d-020c-4079-95af-63bf69da37a5",
            "compactness": "bab6d9c1-892a-43ee-bb39-21115cc5d70d",
            "splitting": "b8e49933-96d2-4c80-a5f2-33e804a1ab57",
        },
        "upper": {
            "proportionality": "38b5edd7-d8db-4350-b531-aebbf33457e1",
            "competitiveness": "eea15926-f43e-4474-ac61-916c4d44ee2b",
            "minority": "c45ee097-233d-4318-964f-56183975e1a3",
            "compactness": "f2ae32c1-d42e-46b1-bd67-92f2e62db334",
            "splitting": "b1bcdf8a-d628-4f6a-b655-7c60c067a775",
        },
        "lower": {
            "proportionality": "59025a15-c795-4a57-981d-bb94cd24bc7e",
            "competitiveness": "84f8e53e-dc0a-4357-9b14-be372522f5b9",
            "minority": "9b452a1b-75e1-46fe-9065-0c368152a212",
            "compactness": "59025a15-c795-4a57-981d-bb94cd24bc7e",
            "splitting": "59025a15-c795-4a57-981d-bb94cd24bc7e",
        },
    },
    "KY": {
        "congress": {
            "proportionality": "e4a2a4c6-d06a-4957-b8d9-36e54b39ef9e",
            "competitiveness": "e4a2a4c6-d06a-4957-b8d9-36e54b39ef9e",
            "minority": "23934d4e-84dd-4316-82aa-0262a28feaf4",
            "compactness": "3a541d7a-192a-451d-a8bf-e01687292adb",
            "splitting": "97a0e7e7-6f03-48a3-a5a7-5a5688755499",
        },
        "upper": {
            "proportionality": "11e0c4eb-15f1-4466-a6b7-638cddc19c7f",
            "competitiveness": "11e0c4eb-15f1-4466-a6b7-638cddc19c7f",
            "minority": "a986aaba-7298-429f-a54b-e3014e773d2c",
            "compactness": "8126a351-8bb7-4c6f-ac73-729fec2a2138",
            "splitting": "a4b7ecee-5eef-4f39-8bad-9bbccfa18e96",
        },
        "lower": {
            "proportionality": "71c7599e-6d15-484f-9d68-e589f6381465",
            "competitiveness": "6b5c4401-6d65-4941-8e5c-98244d7ba0ff",
            "minority": "3376f130-46ed-48a5-bf4d-6082e0f67e6b",
            "compactness": "65ee6d98-198f-4992-8383-431efca5275b",
            "splitting": "cf66cbfd-a3c6-4f77-86a0-5835392d8884",
        },
    },
    "LA": {
        "congress": {
            "proportionality": "599ad941-d7a2-484d-99bf-302d608ab654",
            "competitiveness": "9717fc2f-d4b6-4752-a885-471f5a046845",
            "minority": "599ad941-d7a2-484d-99bf-302d608ab654",
            "compactness": "82a5ff40-4902-4122-80b2-e4bd53308b92",
            "splitting": "6a48ae52-e5ae-43d5-9b3a-f2859d5ef8bf",
        },
        "upper": {
            "proportionality": "13b25a24-b7da-4d5b-95d0-994d97f3e666",
            "competitiveness": "4e7964ad-927b-4060-9845-f29a8048ee96",
            "minority": "8613a759-217e-43f4-9dd2-ee7b9dff9af6",
            "compactness": "25653b73-689a-4082-998b-7b1f6c774d2b",
            "splitting": "eb611cb4-8063-4f98-809c-f22d2e76cfdc",
        },
        "lower": {
            "proportionality": "ac66fb72-278a-40a7-b5e8-a4aa7ee21c38",
            "competitiveness": "70c69238-290d-479b-9c48-8caa1b4b0de9",
            "minority": "329114e6-9c8d-44d8-8983-9729e23d2f09",
            "compactness": "ac66fb72-278a-40a7-b5e8-a4aa7ee21c38",
            "splitting": "ac66fb72-278a-40a7-b5e8-a4aa7ee21c38",
        },
    },
    "ME": {
        "congress": {
            "proportionality": "48ee6b7b-9617-4731-ac62-a559eca9fa90",
            "competitiveness": "155378ea-ca13-474b-8c07-dac52a442513",
            "minority": "35c9a45d-c06d-4237-a397-8a4b54b2390a",
            "compactness": "715a1507-9edb-4e0a-a1e6-76c7733f6c6d",
            "splitting": "155378ea-ca13-474b-8c07-dac52a442513",
        },
        "upper": {
            "proportionality": "584bcb89-67e0-49a7-a803-500adac99150",
            "competitiveness": "584bcb89-67e0-49a7-a803-500adac99150",
            "minority": "584bcb89-67e0-49a7-a803-500adac99150",
            "compactness": "e9c089a4-f687-4887-a79c-bfc21dd0f495",
            "splitting": "fcef0b3c-a79b-41bc-93e4-74cd0d1e8a57",
        },
        "lower": {
            "proportionality": "8744d00a-d573-4e95-92f1-9fc1440ec814",
            "competitiveness": "133dfe57-381e-4200-8f9e-a4998c3b6632",
            "minority": "133dfe57-381e-4200-8f9e-a4998c3b6632",
            "compactness": "8f7d515f-a562-40ed-a3e4-0cb88dca0388",
            "splitting": "133dfe57-381e-4200-8f9e-a4998c3b6632",
        },
    },
    "MD": {
        "congress": {
            "proportionality": "e3e93c31-764c-4ce3-9bdc-6ee3c945df9a",
            "competitiveness": "ca7baeb6-3b84-4edd-bf50-a48ba95e4104",
            "minority": "d8dc1ebe-058c-403a-926a-e5bd560369b4",
            "compactness": "2a9b5438-2740-4980-918e-099050b3df94",
            "splitting": "70801f37-715e-4e7c-b203-c7789c244d4c",
        },
        "upper": {
            "proportionality": "fcbb1f57-4dcc-4263-a041-52a430b3e867",
            "competitiveness": "157e80e5-2fcc-4e8b-8ec2-3c59f22404c0",
            "minority": "454310ca-398e-4f24-9926-39738481296b",
            "compactness": "3835836c-d433-4f36-be67-743d04349075",
            "splitting": "fcbb1f57-4dcc-4263-a041-52a430b3e867",
        },
        "lower": {
            "proportionality": "da938536-4fb7-4a26-ba97-dff856c467e9",
            "competitiveness": "c7345d9e-2692-40d9-8ecb-6b6f24a82c6f",
            "minority": "916610b7-7304-464b-8506-cef3ce5ef1c7",
            "compactness": "da938536-4fb7-4a26-ba97-dff856c467e9",
            "splitting": "da938536-4fb7-4a26-ba97-dff856c467e9",
        },
    },
    "MA": {
        "congress": {
            "proportionality": "8ebc9f02-2286-435f-b634-4416277d4642",
            "competitiveness": "127a0acc-b4c4-4ba5-b25f-c40ee642a468",
            "minority": "9802254e-fda9-4184-8960-28c7191cb76e",
            "compactness": "ba1cc8ea-fe2e-4b0b-9e63-534d40037e5f",
            "splitting": "fffc7551-b217-43b3-86aa-0875c76f4549",
        },
        "upper": {
            "proportionality": "0c9a92d2-f219-44aa-a167-7b21624927d4",
            "competitiveness": "834a703e-db9a-40c8-86d1-1b206ccbe71e",
            "minority": "2ae4240d-6b33-4b07-b96c-bc1bbd3455aa",
            "compactness": "575d775a-ebad-4433-aebe-c9c58885cbd8",
            "splitting": "794bd309-bccd-4d34-9dab-91859f2c1103",
        },
        "lower": {
            "proportionality": "971ed6fd-5cc7-47a4-9840-e1373a272b25",
            "competitiveness": "213b67e3-2cb6-4441-b80a-b057d7a4baf8",
            "minority": "1a33c853-d979-4ff5-9662-bafe906397df",
            "compactness": "d99abd5d-7517-467f-a2f1-b6025e38f6f0",
            "splitting": "971ed6fd-5cc7-47a4-9840-e1373a272b25",
        },
    },
    "MI": {
        "congress": {
            "proportionality": "8219647c-adea-457f-bde8-5730988d7a4e",
            "competitiveness": "90ffd37b-e02f-40d2-a012-d256eb67bb31",
            "minority": "3f3dba13-eed8-4d4e-a0af-6a2573d4d1e8",
            "compactness": "8a8ae70f-2d38-4294-a50e-40fdedd426c0",
            "splitting": "90d9db72-072f-4f08-a238-e5fa67945bd5",
        },
        "upper": {
            "proportionality": "ba410f3b-b7df-4ef9-aa95-49da542816f2",
            "competitiveness": "12816793-fc92-4612-bf5b-e0a0246cf7ea",
            "minority": "1e40fb93-b2d0-4a51-a4f8-8a561ead42fc",
            "compactness": "ad40c618-5a16-45df-a7a0-e7c1a63536dc",
            "splitting": "473b5ebc-17c0-493a-a95f-a73ca3a8b5f0",
        },
        "lower": {
            "proportionality": "186dfea5-b9db-470f-827a-1474a3d89f72",
            "competitiveness": "82c89539-1def-438a-9c3c-61fa8612768c",
            "minority": "1c794e24-717f-46b8-8ba5-2e5d0b0cc8e5",
            "compactness": "d476eba3-fea4-4ffa-ae44-539558166c74",
            "splitting": "9e2a9af2-42ed-462e-beff-6a6fec10ff0e",
        },
    },
    "MN": {
        "congress": {
            "proportionality": "5311ec34-89da-4c79-87d2-f876ee0980b9",
            "competitiveness": "1db8c126-aba5-41b5-bc67-62a20519eda6",
            "minority": "b30cd514-3a83-45f7-bc86-b882fba0ddce",
            "compactness": "7ae6f55a-3672-4c87-a9af-9a3819ecd10a",
            "splitting": "e73c51a1-81b2-4204-897a-b873782fb2b1",
        },
        "upper": {
            "proportionality": "d0404ef7-cd16-4ec2-b9cb-77ea30d7c5a7",
            "competitiveness": "c2d6d121-16b3-49fa-baf5-ab34c326e86f",
            "minority": "583bfff2-bc54-4932-838b-6195d21dd92b",
            "compactness": "cef1d723-2cf1-40d6-8c72-8628a6c74f4d",
            "splitting": "d0404ef7-cd16-4ec2-b9cb-77ea30d7c5a7",
        },
        "lower": {
            "proportionality": "709f889b-6718-4b03-afc3-294aff34c36d",
            "competitiveness": "97f69b3a-30ce-4b82-8dff-7c29d7249ccd",
            "minority": "7a780f28-460f-43fd-9f19-4302d11366c1",
            "compactness": "99d294c7-6f6b-4e87-9b04-47ec899fa75a",
            "splitting": "709f889b-6718-4b03-afc3-294aff34c36d",
        },
    },
    "MS": {
        "congress": {
            "proportionality": "5608c8fc-aa8d-467d-9544-0beca9ceab1e",
            "competitiveness": "3aee6676-fb1f-45a2-a27d-11efa8072d48",
            "minority": "82b998f2-bcb8-40ca-9ad9-b08175937e4f",
            "compactness": "2a668a61-0914-417e-aa14-9439cde735e3",
            "splitting": "205becd2-ed97-485e-8fdd-641980eb062b",
        },
        "upper": {
            "proportionality": "e66d90ec-f254-4360-b610-1f1f52638e02",
            "competitiveness": "051778cf-bc2d-4b5f-aa54-fea68449ddef",
            "minority": "e66d90ec-f254-4360-b610-1f1f52638e02",
            "compactness": "24409017-e724-441c-aafc-05dfb387aa4a",
            "splitting": "51934bde-3b66-4215-874b-e2783c3253b9",
        },
        "lower": {
            "proportionality": "eab9246e-e051-415d-9b03-cc2bac6e4ad6",
            "competitiveness": "8a93ddf6-7203-4a51-85db-1291fd524c18",
            "minority": "eab9246e-e051-415d-9b03-cc2bac6e4ad6",
            "compactness": "62de0be9-7586-4b91-b92f-45632ae06564",
            "splitting": "82d4f534-8cc9-4790-80a3-7f53c5eb6612",
        },
    },
    "MO": {
        "congress": {
            "proportionality": "19037248-b2b4-49ec-a0bd-f0e655ce7929",
            "competitiveness": "36ae7a73-7df1-471b-93a5-cd6b17ff7cc9",
            "minority": "d393f212-17c6-4de0-bf03-8afd288c5234",
            "compactness": "35607bfd-2363-421b-8a0e-ec8252bcc4f0",
            "splitting": "bc401ba3-2df8-4ee0-be9a-5beb5263c1ce",
        },
        "upper": {
            "proportionality": "9e491e6b-5d8d-48c0-8418-5533ff8ea1d7",
            "competitiveness": "c80f89ad-a785-4d7d-b2fd-11b1095e989e",
            "minority": "9e491e6b-5d8d-48c0-8418-5533ff8ea1d7",
            "compactness": "bc67d7f8-0225-4fef-843c-75eb03f83e10",
            "splitting": "415807ea-9e88-48df-b90d-9b49a516aab1",
        },
        "lower": {
            "proportionality": "2949b0f5-375a-4af4-b831-3a52dd2a2e61",
            "competitiveness": "7c9e8a94-6d32-4571-bd51-d7db73d4993e",
            "minority": "5487c209-0a55-4663-b221-eeb4fce71bf1",
            "compactness": "2949b0f5-375a-4af4-b831-3a52dd2a2e61",
            "splitting": "2949b0f5-375a-4af4-b831-3a52dd2a2e61",
        },
    },
    "MT": {
        "congress": {
            "proportionality": "1c2dab29-bba4-430f-b4c8-0fcac86606ad",
            "competitiveness": "0f8e275c-6e48-4c61-b194-a0fd629daa3b",
            "minority": "1c2dab29-bba4-430f-b4c8-0fcac86606ad",
            "compactness": "a9bbc437-2180-44fb-8d47-3749e1d6a183",
            "splitting": "1c2dab29-bba4-430f-b4c8-0fcac86606ad",
        },
        "upper": {
            "proportionality": "9f92c00e-476c-4307-a550-8f7eee8a1f73",
            "competitiveness": "ffe44d05-632d-4930-8fd4-2d06ff47dc53",
            "minority": "02f06484-b0fd-4872-8adf-df40967de5d8",
            "compactness": "9edfd087-8f70-4b6c-bece-ea650e4cf41b",
            "splitting": "1e70d207-f960-4226-b8bc-38ef47e6fe8e",
        },
        "lower": {
            "proportionality": "502bd8e2-4a9a-4204-9eca-892df3625ba7",
            "competitiveness": "59ab831d-1060-4c8e-a807-31912b6906da",
            "minority": "5a912a7b-7177-43d9-b019-1962132a4827",
            "compactness": "7974b7ba-0425-4dfc-956a-b1ef864b9f3b",
            "splitting": "f6c6bdd2-f862-480b-9d23-325886973b9d",
        },
    },
    "NE": {
        "congress": {
            "proportionality": "a24298eb-b222-49ba-ae6d-f598980bd20d",
            "competitiveness": "e3661060-744c-4537-be9b-1831aa2235ad",
            "minority": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
            "compactness": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
            "splitting": "e3f66393-18fc-4d37-9599-32411ad2bf20",
        },
        "upper": {
            "proportionality": "060de2ad-5828-4587-a614-9d24c6a931fe",
            "competitiveness": "d973b425-2938-477a-9787-2e0532c8cd99",
            "minority": "310af3b2-3334-4eb7-90eb-033960de9ba3",
            "compactness": "3881bf9b-6655-45e7-b5fc-bbc4ee1bb194",
            "splitting": "4fe39d2a-8b93-47fc-a0b3-035ffb06232c",
        },
    },
    "NV": {
        "congress": {
            "proportionality": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
            "competitiveness": "386c21f7-d519-44c2-b377-d26097ee1ff6",
            "minority": "e7a2f9aa-33d1-45c9-a0f3-5b3e8ce6ac5a",
            "compactness": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
            "splitting": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
        },
        "upper": {
            "proportionality": "bfcef554-b7c7-445d-b7f7-8b6092d993f6",
            "competitiveness": "24f2d2ef-547c-490d-b0c9-6d62052a7c49",
            "minority": "1cc3027d-9540-4594-973d-325ff429b096",
            "compactness": "4b7b2e8e-828f-41cf-ba94-249100206261",
            "splitting": "7ad68bce-89b6-4a46-ab73-1313ce0dbc94",
        },
        "lower": {
            "proportionality": "17c9031d-40af-4558-8aa7-52057b1bb1fd",
            "competitiveness": "51d3a9f3-ba0e-40ec-bbf9-1ae6af7145e1",
            "minority": "6cddcece-3797-43f6-8024-76958463ca50",
            "compactness": "ad866cf4-1cac-45e0-956d-8e3003184e1f",
            "splitting": "3b430175-24f6-4b11-8c4a-b230adc9d186",
        },
    },
    "NH": {
        "congress": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "upper": {
            "proportionality": "aadb0e1b-68b7-4d3d-b987-db3d37e787aa",
            "competitiveness": "34386ec1-707e-42f3-a0a7-eec4598cc02e",
            "minority": "978a8339-900d-4c10-be7e-be08232aed0f",
            "compactness": "613e93e3-f9bf-43df-8a19-62e4dcdb6c20",
            "splitting": "a7000b87-d5b7-443b-8a0f-01ddbc77ac8d",
        },
        "lower": {
            "proportionality": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
            "competitiveness": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
            "minority": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
            "compactness": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
            "splitting": "b20f0257-5cc1-4733-aca8-1fb9e412cbd7",
        },
    },
    "NJ": {
        "congress": {
            "proportionality": "b0263350-1c50-4a24-bc94-60422487fec6",
            "competitiveness": "c58000d6-4f38-4e79-9843-25c91fcf1cfe",
            "minority": "1f2e6cb7-61aa-4a8b-8800-38ce8a767248",
            "compactness": "6fcb6b8b-2565-4831-990f-b978b88cc253",
            "splitting": "c24cf3a7-541a-472a-9e3f-6ebe398e8c33",
        },
        "upper": {
            "proportionality": "db9a23bc-a9c7-4db3-a5fc-b4d081a7d07c",
            "competitiveness": "cd90f252-5b7d-465b-a172-70f2880cc287",
            "minority": "e284de6e-8507-4be8-b87a-a0a6f18efd3d",
            "compactness": "0c974b16-9c2a-489e-acf4-e18227519c6f",
            "splitting": "ecacb42d-dbbe-4518-b7c6-11624c3dbb04",
        },
    },
    "NM": {
        "congress": {
            "proportionality": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
            "competitiveness": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
            "minority": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
            "compactness": "714b1ebf-9280-463a-b02e-e1781196dd3a",
            "splitting": "1346fd58-88f2-49fd-a653-74c46813549a",
        },
        "upper": {
            "proportionality": "94ccc634-e4d7-414c-bc6e-a849e4fe5245",
            "competitiveness": "502f677f-7727-4872-8c9f-bc63b3a22f78",
            "minority": "94ccc634-e4d7-414c-bc6e-a849e4fe5245",
            "compactness": "cac69b2f-3397-48c4-98bf-189810a7f0bc",
            "splitting": "27dd5147-d618-44c7-9abd-84c493a2787b",
        },
        "lower": {
            "proportionality": "fe2112cf-c590-48f6-8fef-4da504d0a96e",
            "competitiveness": "95987f22-bff4-4739-b6b6-55335c6d98c5",
            "minority": "fe2112cf-c590-48f6-8fef-4da504d0a96e",
            "compactness": "10a8c843-b571-4238-85a0-378c9116e2bd",
            "splitting": "fe2112cf-c590-48f6-8fef-4da504d0a96e",
        },
    },
    "NY": {
        "congress": {
            "proportionality": "4859f08f-1421-4308-8594-a92ee8ffca37",
            "competitiveness": "5c38386f-c06e-4563-89c3-58311ecece28",
            "minority": "fe733d47-6219-48ad-9a61-3a3933da7e61",
            "compactness": "e539026e-16e8-46ce-8f91-0d13ccf03986",
            "splitting": "03ae2d7f-27d9-47b1-97e8-5bed81f428e2",
        },
        "upper": {
            "proportionality": "b3fa5809-5631-4a99-ac9a-898dda969d1d",
            "competitiveness": "49352ea2-20a9-40a2-9646-956bc06f71be",
            "minority": "11bf9bdd-9f1f-43c5-a8bd-2544b529e821",
            "compactness": "af7b1cfa-1329-40ac-ae60-8c4622965c2a",
            "splitting": "d3f039e4-ddb5-4275-9c98-079e6a7dd56f",
        },
        "lower": {
            "proportionality": "43cd4d4c-214b-4045-b22b-eafab9076fee",
            "competitiveness": "90e3d9a0-67c4-4996-b6a5-b27992921977",
            "minority": "93de1fa3-c977-4b4c-ab5a-c2b9b9107158",
            "compactness": "e4b0af09-a675-4d23-b9bd-415accd86ede",
            "splitting": "1969b461-9aa9-476d-a178-b888b4cd284d",
        },
    },
    "NC": {
        "congress": {
            "proportionality": "ffbd1339-0707-4efa-a791-158eef599367",
            "competitiveness": "72b79b26-ece6-429a-ae8e-185908bf9e90",
            "minority": "131c0896-4040-4cc6-bf39-fef558fdc99f",
            "compactness": "2bfb3e38-ae0f-4304-b056-80b7c261bf85",
            "splitting": "34f3965f-566b-46b4-a70a-6d99de7e6244",
        },
        "upper": {
            "proportionality": "4f406384-c1c4-4aab-820b-4a2a866be7cc",
            "competitiveness": "18a27f49-e858-4eb6-86de-8bba06217d3b",
            "minority": "5eaf36ca-1951-474a-ad7d-5004ea38ad66",
            "compactness": "5484bf1f-a68a-4fce-b47b-f5db88fa988e",
            "splitting": "a34f8f88-5ef2-474d-beaa-3fce75d70b59",
        },
        "lower": {
            "proportionality": "82194147-3f8d-4dc7-9740-2adfaa9f6f1b",
            "competitiveness": "155c4189-6dcf-406f-9163-f5c3a47f6f00",
            "minority": "28c55529-c8c5-4e83-aab7-73500625cd3d",
            "compactness": "16e266ce-3407-4c71-8b7e-4551973503a7",
            "splitting": "82194147-3f8d-4dc7-9740-2adfaa9f6f1b",
        },
    },
    "ND": {
        "upper": {
            "proportionality": "dd632c2c-d10b-4288-8332-19cbdb2428df",
            "competitiveness": "684b360b-8653-4547-9548-0b165a5c9d85",
            "minority": "feaaff73-0a6c-49cc-8772-4d90848a85ae",
            "compactness": "38bab00f-2a54-4b2f-881d-01dd63521667",
            "splitting": "feaaff73-0a6c-49cc-8772-4d90848a85ae",
        },
        "lower": {
            "proportionality": "f45d516e-1a36-4fd8-9a14-b0c8fa4825d1",
            "competitiveness": "11cda076-c708-44d5-b4bb-9ff15abce6cd",
            "minority": "11cda076-c708-44d5-b4bb-9ff15abce6cd",
            "compactness": "0310961c-0fc9-4cd1-8026-6cb0a8e58457",
            "splitting": "f45d516e-1a36-4fd8-9a14-b0c8fa4825d1",
        },
    },
    "OH": {
        "congress": {
            "proportionality": "b574d8b5-8376-4f84-bb1f-6c1d75deb605",
            "competitiveness": "2ce86262-30c9-4aad-b1d5-e298f548d0c0",
            "minority": "a4830abd-f07f-4846-89f6-da1b822c007e",
            "compactness": "b574d8b5-8376-4f84-bb1f-6c1d75deb605",
            "splitting": "e1133ef6-020c-4f0f-b58d-8f11fb6ae084",
        },
        "upper": {
            "proportionality": "90313866-c4b5-45bb-856b-a1428cd9166a",
            "competitiveness": "229c5394-b60c-405c-bad7-5baabe790d64",
            "minority": "1ace05fd-3a47-4dc2-9c28-eef62123dd89",
            "compactness": "92e39f5a-59a8-4c6c-b18f-7d7bf9f50b56",
            "splitting": "de428c54-5877-44e4-afba-8009c36ea427",
        },
        "lower": {
            "proportionality": "df74d344-6293-4ced-ae21-2e755768089d",
            "competitiveness": "838e26bf-368b-44be-a2d4-9aea1e729c62",
            "minority": "df87780d-1c89-49eb-9e2f-3260f7f3c115",
            "compactness": "df74d344-6293-4ced-ae21-2e755768089d",
            "splitting": "df74d344-6293-4ced-ae21-2e755768089d",
        },
    },
    "OK": {
        "congress": {
            "proportionality": "bdb778a1-ae0c-4ac9-9277-bf70512a14c9",
            "competitiveness": "7f101a2e-08e2-4ef0-8af5-b7a8b4ee04e7",
            "minority": "c42edda8-9784-4c3e-ad11-ba3512ee0845",
            "compactness": "10e4bc47-38a4-4b0d-9329-81b40bc039f4",
            "splitting": "e0896099-b746-404e-b4f9-bfee04fee59f",
        },
        "upper": {
            "proportionality": "4d2f1edf-138b-46eb-ae1e-ff26187b0815",
            "competitiveness": "e74d3240-067d-486e-bd66-a638a2ae8739",
            "minority": "6a5d5415-3007-4f1f-9455-0c903c33108f",
            "compactness": "fda01cd4-e4c5-4251-9254-22d6cb660561",
            "splitting": "a0252030-b09a-46b6-b3e5-2d89ee505dc8",
        },
        "lower": {
            "proportionality": "bf1b734a-8ec3-4f70-b259-64863043ae4a",
            "competitiveness": "bad38fbc-4cf9-4bb0-9395-cf6817478443",
            "minority": "bb90fd5d-c2c1-4b3e-82ac-3a83a8417222",
            "compactness": "a3f21121-d8ce-4984-88fd-baeacde77e47",
            "splitting": "bf1b734a-8ec3-4f70-b259-64863043ae4a",
        },
    },
    "OR": {
        "congress": {
            "proportionality": "2ec63ab0-0c5f-4b4b-af67-87dce0250e58",
            "competitiveness": "207843ca-3f94-4c8c-a3bf-7f59169094ce",
            "minority": "20fd1b1a-f146-4621-b2f0-5686329f72bc",
            "compactness": "da0b87bf-a018-4c5f-9c62-bee1b6501626",
            "splitting": "aec42732-bee0-481b-a632-99d76d3a1482",
        },
        "upper": {
            "proportionality": "05ca44e2-fb0b-423d-8909-6cd81f95133c",
            "competitiveness": "529e960b-cef6-44fe-97d9-cbcb7e59e3af",
            "minority": "2d30318a-2b8d-469f-8429-e93b383281f8",
            "compactness": "92afb2ce-2435-4cc3-9d89-1863db65044f",
            "splitting": "bd75b153-3730-42d3-af5c-9d134074a10f",
        },
        "lower": {
            "proportionality": "da395e3f-50b0-4216-95a1-bd381eab3d88",
            "competitiveness": "0ce5a943-5606-4c6d-a33f-5805b9ba8362",
            "minority": "199a2873-5d44-4c96-8524-fed2c38b05a1",
            "compactness": "43c6f925-3763-40f3-a03c-58db3223a6ef",
            "splitting": "bd6a7b8a-b325-42b5-84be-24d351e4e6b1",
        },
    },
    "PA": {
        "congress": {
            "proportionality": "5f827f23-b7b2-4e69-aee6-d7ad42e63bdb",
            "competitiveness": "8d127230-6295-49ae-a312-11700e0b7a36",
            "minority": "4babf6a6-4420-4652-b1fa-179dd520cea6",
            "compactness": "a9833d3e-3fad-428f-81da-4912601b11b2",
            "splitting": "5f827f23-b7b2-4e69-aee6-d7ad42e63bdb",
        },
        "upper": {
            "proportionality": "d4087dc0-7336-4da1-9252-1def1cab5160",
            "competitiveness": "e0ea3cc7-02a2-4647-a864-2ed207eca57f",
            "minority": "e1836c6b-77d8-4cd8-9660-88b10389cb9e",
            "compactness": "6e67747b-7656-43d1-8c9b-513a3049935b",
            "splitting": "3be63721-f0ec-4873-8b85-55b0cc0448ef",
        },
        "lower": {
            "proportionality": "240dcf5b-7e0a-4fd4-a5d9-7a25fbff4e9d",
            "competitiveness": "d81a6b9b-0d38-49d9-9ff2-988aec0b951d",
            "minority": "735614b3-98a5-4d2c-a871-4ac0c7a8da82",
            "compactness": "bcc078df-547b-498f-8ea1-a7ec6e7953cb",
            "splitting": "240dcf5b-7e0a-4fd4-a5d9-7a25fbff4e9d",
        },
    },
    "RI": {
        "congress": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "upper": {
            "proportionality": "c067a443-87ba-488f-8017-ced48d9bff29",
            "competitiveness": "c067a443-87ba-488f-8017-ced48d9bff29",
            "minority": "c067a443-87ba-488f-8017-ced48d9bff29",
            "compactness": "c067a443-87ba-488f-8017-ced48d9bff29",
            "splitting": "c067a443-87ba-488f-8017-ced48d9bff29",
        },
        "lower": {
            "proportionality": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
            "competitiveness": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
            "minority": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
            "compactness": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
            "splitting": "58f9c5c7-4356-4cd9-a006-b6a66568c049",
        },
    },
    "SC": {
        "congress": {
            "proportionality": "f85fa8fe-8e77-4fca-967f-c25eba448ab1",
            "competitiveness": "bea590c5-ff76-4638-89e5-4a9990da6b51",
            "minority": "15b06901-9f52-438a-9186-cb353d715489",
            "compactness": "d2e93d7e-986c-478b-a91e-11aa49df9fa4",
            "splitting": "14fb2ae8-9e79-45d9-8492-30c07511a107",
        },
        "upper": {
            "proportionality": "8d043b67-4d5f-4a89-a339-d632c6be1624",
            "competitiveness": "1fc5a405-e89f-4b7e-863a-b75b241aa383",
            "minority": "6f0c8482-b774-485a-90e9-e1b591aefe30",
            "compactness": "b700103a-362a-49ef-8025-361eae3b6241",
            "splitting": "1ead237d-42a1-476a-b5c9-61e7bf4963db",
        },
        "lower": {
            "proportionality": "45bb621d-2f91-4059-8f7e-ca6b7ff6d8f0",
            "competitiveness": "16d67589-ae59-4939-897a-eacebdd940a1",
            "minority": "60562401-be91-46e2-a4a4-de6b681e5ac5",
            "compactness": "9868a21e-2f73-455d-84c3-274924ed0031",
            "splitting": "659ba563-8c55-4422-98d3-d8211a8883a0",
        },
    },
    "SD": {
        "upper": {
            "proportionality": "9b855b81-e574-435d-80fe-b43052679127",
            "competitiveness": "faf97f72-98a1-4f27-b7c4-a2986300fd94",
            "minority": "e12c309c-626b-46ef-bd1a-6e2d1797fce7",
            "compactness": "e65efa94-2003-451c-b0fb-f2cf579bc0d7",
            "splitting": "7ee4fe90-e1fd-4c5d-9440-832d6ffb76b6",
        },
        "lower": {
            "proportionality": "cf2be840-5e79-4578-9804-799165cc01c5",
            "competitiveness": "4f4d5a65-0362-41ab-87d8-267a0720595f",
            "minority": "cf2be840-5e79-4578-9804-799165cc01c5",
            "compactness": "8333718c-ff59-4019-8b81-90ecd2863c99",
            "splitting": "8333718c-ff59-4019-8b81-90ecd2863c99",
        },
    },
    "TN": {
        "congress": {
            "proportionality": "634fc0d2-0592-48e3-b626-d313bedb7e94",
            "competitiveness": "4bc62ac0-a13f-46d0-93b9-fc399e778791",
            "minority": "ba926689-4308-4a3f-9283-ce554e22399e",
            "compactness": "7e82c761-c16f-442f-ae69-72480e4c903d",
            "splitting": "32587b8e-f18b-463f-8f30-86a3fdbb8bd7",
        },
        "upper": {
            "proportionality": "126a54db-d5b8-416f-a7b6-6cb245753c6a",
            "competitiveness": "46140d63-e622-422d-9cc0-2f10a2a06ea2",
            "minority": "371a6137-660e-490d-a64e-dad4c2d0e5bc",
            "compactness": "bbbc2f72-5e97-4f48-893f-39330d255225",
            "splitting": "033588cf-8dc7-4615-bd3f-574a3197814f",
        },
        "lower": {
            "proportionality": "deb43161-d092-41b6-8d67-1380237b5860",
            "competitiveness": "bc4b2ef2-71ca-4ac0-8c3f-0e040af97197",
            "minority": "74b29e0d-1990-4f7e-a242-788d1b399b93",
            "compactness": "deb43161-d092-41b6-8d67-1380237b5860",
            "splitting": "deb43161-d092-41b6-8d67-1380237b5860",
        },
    },
    "TX": {
        "congress": {
            "proportionality": "999d3d10-cb97-442c-822a-797bb9f1ec09",
            "competitiveness": "17676986-5ed9-4be7-a565-bf24aa686ad0",
            "minority": "ae7aedd8-ada8-423b-86cc-31d80e51f8a4",
            "compactness": "cb1adf0f-0e1d-49fb-985b-40035825185c",
            "splitting": "302bdd12-5b1a-450a-8d56-8ca6116dd547",
        },
        "upper": {
            "proportionality": "b8a4c3b6-157d-4769-be38-890f23a9ac08",
            "competitiveness": "b2d59226-98d6-4373-8afd-049c4cf4f429",
            "minority": "a3c67fa3-f0e8-478d-95d3-a330425078c7",
            "compactness": "f059154d-1727-4cad-96f9-c70f57fc3002",
            "splitting": "97a2e7b9-f31e-43a2-bdbe-71f29c38ae21",
        },
        "lower": {
            "proportionality": "7cf4ce61-d71a-4651-a59f-4251b03d4ead",
            "competitiveness": "8d0a5a2f-3a37-4600-a825-8f89bc7b6d00",
            "minority": "481806fc-50c0-4c0d-ab98-94a0c5904b0c",
            "compactness": "647eb4ea-aeaf-4b65-bf43-6ae8bcd01a17",
            "splitting": "aaaaf544-f285-4352-ac67-5a6308c2bb5a",
        },
    },
    "UT": {
        "congress": {
            "proportionality": "0ed784fd-4f1b-4959-96e5-27ce3390ec75",
            "competitiveness": "ca6205cf-c947-4227-b5ab-521077f1c690",
            "minority": "5ad8b01d-bf98-4db2-976e-8df3bbdf2c1d",
            "compactness": "0ed784fd-4f1b-4959-96e5-27ce3390ec75",
            "splitting": "0ed784fd-4f1b-4959-96e5-27ce3390ec75",
        },
        "upper": {
            "proportionality": "de24cd62-9c88-4811-9ffa-264684e43fb3",
            "competitiveness": "03a5b088-bfec-4f2d-9e80-3765dd3b6097",
            "minority": "abb2df53-14c4-4bc9-bb03-60c141a0e01d",
            "compactness": "90d9b07d-33a8-4d0d-9ba0-993c2b080bb6",
            "splitting": "d2c2c842-f009-450c-b14e-73f41d1768f2",
        },
        "lower": {
            "proportionality": "32dd49b0-3c49-4abe-8cc1-de9741838d7c",
            "competitiveness": "f1dcd3ac-131a-4986-8fd9-b7a886d594d7",
            "minority": "61b4d339-b573-402d-9bb0-c3926d2fc86a",
            "compactness": "32dd49b0-3c49-4abe-8cc1-de9741838d7c",
            "splitting": "32dd49b0-3c49-4abe-8cc1-de9741838d7c",
        },
    },
    "VT": {
        "upper": {
            "proportionality": "b1ff9415-468b-45a1-8cc0-807c75a781b3",
            "competitiveness": "f0cc4975-e6e3-4703-837d-9317304553d9",
            "minority": "3570537a-4b97-4742-9bff-9490b81aabf0",
            "compactness": "3570537a-4b97-4742-9bff-9490b81aabf0",
            "splitting": "03476555-253c-436e-9c45-c12d33ae84a1",
        },
        "lower": {
            "proportionality": "9f998929-e47f-4824-aff8-3e76855f0676",
            "competitiveness": "9f998929-e47f-4824-aff8-3e76855f0676",
            "minority": "44acc15d-6a91-4498-b905-cbcd32ed9d2a",
            "compactness": "0e7e8f48-6424-4080-8a13-ade8593f8f39",
            "splitting": "44acc15d-6a91-4498-b905-cbcd32ed9d2a",
        },
    },
    "VA": {
        "congress": {
            "proportionality": "3e80b30a-3965-4f9d-95e9-43403b26fe45",
            "competitiveness": "5ac8f092-390b-45ce-a402-e5ecd3d756d9",
            "minority": "b7bca83f-1dc0-45c2-8f82-e15441ff2c81",
            "compactness": "55426dbf-1d87-45ce-b164-77d8ae985898",
            "splitting": "f7922a95-0311-40ca-94dd-0f2651afb763",
        },
        "upper": {
            "proportionality": "c94ed57e-5a8e-4112-ae3c-472dbcd6e574",
            "competitiveness": "05b3e43d-b9a1-429e-b369-f92c1fcc0a88",
            "minority": "8b513276-cbbc-4521-8054-ed795c834a03",
            "compactness": "1a06ee5f-52e3-48da-bf06-b37d1ced756b",
            "splitting": "9de8a52a-d472-46a6-81ea-613346d670f1",
        },
        "lower": {
            "proportionality": "f8f319b7-f317-49ab-80ca-3d279200421d",
            "competitiveness": "78de05da-b244-4124-95e5-6be496703e62",
            "minority": "a68bea11-832e-433a-9e35-c459c350dce2",
            "compactness": "34f5c4a1-1158-4a29-b529-d1911f03f9a6",
            "splitting": "18130de1-15f0-4f00-8640-fd7594548d65",
        },
    },
    "WA": {
        "congress": {
            "proportionality": "2186bb08-36ef-4e47-b408-fcf41e056eb8",
            "competitiveness": "7c0bc9f0-6e1d-4afb-a3e7-c10e61a5a423",
            "minority": "7b82c987-3779-49c3-b1b8-df838580c9aa",
            "compactness": "cab3e806-3015-4e65-8daa-d5267f949046",
            "splitting": "0793bd88-f7c4-4249-bc0b-c530c96eba95",
        },
        "upper": {
            "proportionality": "0a93a937-8c30-4376-9c99-178f5eb6ae19",
            "competitiveness": "0a93a937-8c30-4376-9c99-178f5eb6ae19",
            "minority": "0934b5f1-aa45-44a8-ac07-212de11729e3",
            "compactness": "74cd59a8-eda7-4166-80bf-948fa99fa21a",
            "splitting": "080690d2-c562-4152-aacd-4dc2da6c0aaf",
        },
    },
    "WV": {
        "congress": {
            "proportionality": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "competitiveness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "compactness": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "splitting": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        },
        "upper": {
            "proportionality": "713b4b83-5778-4448-a27c-4f29cc6be90f",
            "competitiveness": "f4b7b7fa-8c8a-4556-b526-c11f21334486",
            "minority": "99b6e18c-422a-4638-8c34-3dc3026b8db3",
            "compactness": "68b9a4c7-c7a6-45eb-8d4a-5e300f22cbb4",
            "splitting": "6f811d1f-18ec-48c4-aebf-34582bcdb1d5",
        },
        "lower": {
            "proportionality": "9a521083-109d-4d83-a612-62b906ef997b",
            "competitiveness": "7d730511-4c75-42fa-be9b-4dd49503be2b",
            "minority": "aefd63ea-afea-4152-8a26-bb349c219683",
            "compactness": "3796ee9b-89ab-45ee-b1da-46fd68fd0d8a",
            "splitting": "82314e82-05df-4487-96b9-22c987131b7a",
        },
    },
    "WI": {
        "congress": {
            "proportionality": "593fc0fd-36b3-43c9-ba1f-1b1bc53c94d6",
            "competitiveness": "298af77b-010e-474a-b99b-653f7808877a",
            "minority": "0db266c6-25c9-424c-a872-6b8e426ae3bd",
            "compactness": "9170bbda-d4a4-4d22-b389-558e90353a0d",
            "splitting": "e86707d2-f00b-4c00-863e-85cc1ee03ce1",
        },
        "upper": {
            "proportionality": "55d665b1-d916-4fe6-9f02-16090fbb1a88",
            "competitiveness": "55d665b1-d916-4fe6-9f02-16090fbb1a88",
            "minority": "31c20c11-335b-4d81-9064-532263d5f395",
            "compactness": "e319d423-9972-4721-9ce3-0df929dcf91f",
            "splitting": "3eaf50fe-5bb8-4d67-b4af-77fb2bf16df6",
        },
        "lower": {
            "proportionality": "8e194afd-a819-4516-aa24-5eb840504984",
            "competitiveness": "3d04f4c3-0fba-4d1f-9478-2aea7d3600da",
            "minority": "2e41de6c-3091-44ff-9f20-b201a448f8fb",
            "compactness": "465c506f-916a-4f7f-8b4e-4b0f865f416e",
            "splitting": "aa699793-da80-4bf7-be29-a080cd9e0dbd",
        },
    },
    "WY": {
        "upper": {
            "proportionality": "0b05d302-cf3b-49b7-a97c-f22a460dfccd",
            "competitiveness": "92e1b23f-7d59-44ea-8e28-b7e8e4cee4dc",
            "minority": "de3df80e-5268-484c-b379-c31b6e57188f",
            "compactness": "1994d9a1-89b2-41ab-9ac8-4db36f71d6d4",
            "splitting": "0b05d302-cf3b-49b7-a97c-f22a460dfccd",
        },
        "lower": {
            "proportionality": "76f6fcc4-4bcb-4b27-9062-723777e63586",
            "competitiveness": "4408cef1-4b9a-4d30-a989-1a0f0482741d",
            "minority": "4408cef1-4b9a-4d30-a989-1a0f0482741d",
            "compactness": "76f6fcc4-4bcb-4b27-9062-723777e63586",
            "splitting": "76f6fcc4-4bcb-4b27-9062-723777e63586",
        },
    },
}

# TODO: Update this
# These are the ids for *copies* of the published notable maps in DRA,
# as well as any changes if the notable map was bad for some reason.
# For congressional plans, see the legacy comments below.
NOTABLE_MAPS_COPY: Dict[str, Dict[str, Dict[str, str]]] = {}


### LEGACY - IGNORE BELOW HERE ###

# - This is copied from constants.py in the original PG repo.
# - Why did I comment this stuff out? Did it become inactive somehow?!?

# - This is legacy metadata, before retooling the workflow at the command line.
# - The ids tell you what notable maps I cloned.

# # Official congressional maps on 11/07/2022
# # Pulled from data/state_plans.json copied the same day

# official_maps: dict[str, str] = {
#     "AL": "b1cfc3f6-27df-498d-a147-0664d75fea88",
#     "AR": "fa3434ec-4f52-48de-947b-5998b6937bf0",
#     "AZ": "4ee8ecf2-14b7-4a8d-99bc-82fa633a9305",
#     "CA": "fc9d2d06-7c7f-451c-92cb-122127a79c29",
#     "CO": "39f44408-23f7-439d-b7eb-923da58b63df",
#     "CT": "707f203c-ce98-4de8-b150-a2605136e015",
#     "FL": "3a6791b9-a186-4691-a95c-5d51dbb3be1c",
#     "GA": "3a370cc7-f820-4af4-8fca-a27ec52502b7",
#     "IA": "628d5e9a-bd35-4248-aa8c-73af095e0135",
#     "IL": "8a4586ad-4c58-489b-828c-4477cfd0ce88",
#     "IN": "c08c9df0-9756-4c5a-a7e7-01ff03bbb170",
#     "KS": "2ea884cd-5687-48b4-879a-4f780d3de1cf",
#     "KY": "0ec1616e-7ed6-4f84-b20d-dcc51221b2bf",
#     "LA": "42873bd9-ce68-4ee1-878e-be420dbf0ee3",
#     "MA": "791f8174-e00d-4baf-9b0a-206a298eb28b",
#     "MD": "a365ecbd-db5f-4c84-a77f-90310c6a6c1a",
#     "MI": "287ace43-1a66-4686-b596-949f578971a8",
#     "MN": "4b212b88-2b8b-48aa-b2d2-e2f9980ac884",
#     "MO": "68b2b598-69cd-430e-bee2-1dc4b76705f6",
#     "MS": "2a63d0b3-58db-4e59-9b3b-436b221e078a",
#     "NC": "6e8268a4-3b9b-4140-8f99-e3544a2f0816",
#     "NE": "9de1188c-2169-4c5a-a4f3-76179d22b279",
#     "NJ": "6ff0b024-2e5d-4e9b-ba0e-56f6de17ea80",
#     "NM": "ec1c76cd-f59f-445b-8f24-fbffb0e8bdf5",
#     "NV": "eb89e40d-595f-485f-9a43-d1bbdd6d0cb4",
#     "NY": "395a7fbe-fa32-47fc-993d-e07d36baff72",
#     "OH": "64d56870-70ea-4f4d-b667-9a4fd60ac511",
#     "OK": "f726bcb3-b750-44b2-9d0b-e2df90fe6fa5",
#     "OR": "9b2b545f-5cd2-4e0d-a9b9-cc3915a4750f",
#     "PA": "b0a94d77-5d99-41c5-bc01-5859a6e1f3e6",
#     "SC": "839561a1-8c15-4c4b-ab56-3275d68092f9",
#     "TN": "445d4976-c994-473f-b14c-4b87464b07ee",
#     "TX": "1c2c1e0d-2fd1-43a8-a039-73e7023124d1",
#     "UT": "b4d46a7e-4366-4f6c-ac54-ff6640d4e13f",
#     "VA": "bc930c25-236f-46a7-bbe9-d8d77e21d011",
#     "WA": "3dd8f07d-8f9b-4905-a155-573bdc084b06",
#     "WI": "aa64c8f5-837c-474f-819f-6eaa1094d776",
#     # States w/ 2 congressional districts as of 07/16/23
#     "ID": "ebc8cec8-b919-4a66-9b42-9cf5bf7e02a1",
#     "MT": "66ff2b64-826d-48a9-bbe4-08afa4c10873",
#     "NH": "a1a2b285-f862-402c-9e89-b45791a46473",
#     "RI": "cffbb279-824c-47b8-90c7-3070378e37ae",
#     "WV": "aaaa571f-f204-4cbe-bcf1-404db0519d36",
# }

# officials_copy: dict[str, str] = {
#     "AL": "8c611540-7cb1-424c-b6b9-7ddc7f39abeb",
#     "AR": "bba50394-d34c-4f0d-9056-8b9e6a029bfd",
#     "AZ": "4a3d07fd-382c-441c-9c8d-af5d52987b87",
#     "CA": "4daa293f-a347-4ba0-926e-3caebce864ea",
#     "CO": "1d2c7749-d9bc-47b3-971f-e8025cc6d1da",
#     "CT": "22a81014-0b6f-407d-acfa-99f464ed1039",
#     "FL": "2e7debf0-c99b-4b54-9b99-df65d413d629",
#     "GA": "e61aaae9-8af9-4339-8959-9c27f02e55d4",
#     "IA": "ccbacbb9-dac8-4c48-b30b-42b0a6627e8f",
#     "IL": "a5e1ee97-3727-4be1-80c7-8bfa7c72ee13",
#     "IN": "da195dcd-381e-4598-bae4-9dad2ea12a8d",
#     "KS": "cd94aec1-6e84-48d6-8922-5eea4f4c471f",
#     "KY": "b38aeac3-297e-4ec4-9073-66215b9763c1",
#     "LA": "a56db05b-6066-4cdc-89f3-e0b12ab7ea37",
#     "MA": "8b9bdb2d-da5e-43db-acf1-08175c1718ba",
#     "MD": "96d5e235-58de-4a46-a443-f5b6fabe0244",
#     "MI": "55420ff6-a8a2-4291-afb3-6ec8c93e6872",
#     "MN": "b382eee8-0eb8-4b5c-a9bb-7886972ed6b7",
#     "MO": "57337b6a-45fc-4ee4-97a1-11540fd6c8a6",
#     "MS": "7edecbd8-cdc5-4972-bcab-07bbd38259bb",
#     "NC": "7b11a99a-6418-44cb-bc0e-ab5e040f6bae",
#     "NE": "413dfcb2-0ec6-4459-9e3b-7cef2ddd8638",
#     "NJ": "1f7c8393-0b8a-49ea-8fb4-60c393cfb661",
#     "NM": "d2db917f-b700-4738-9a93-a38a43630c86",
#     "NV": "c4077907-6605-4fd3-9493-50527ceee352",
#     "NY": "11dc2c25-27a6-4259-b3dc-8e24fa21a086",
#     "OH": "8290f680-abf8-4877-84a7-6075b31f9468",
#     "OK": "bdd4c054-9a75-4117-9819-18673c1f9412",
#     "OR": "9255d54b-36cc-4ca2-972d-fc330c975990",
#     "PA": "bca4620c-bc4a-457e-a472-631ac20c3389",
#     "SC": "68e91af2-1a68-4bc7-aa85-a48e52f07da3",
#     "TN": "e142df57-8dd5-44c3-a316-c2675e0e2fe4",
#     "TX": "89c7b67a-6164-42ee-89d4-072a4fca82c1",
#     "UT": "a2845eee-af70-4c54-944f-08abd5b05471",
#     "VA": "837303a3-ac0a-4fe3-b99e-b4e98f71d26a",
#     "WA": "be06fce9-90a2-4bc0-9659-8eacafcd4afc",
#     "WI": "130feb94-6532-4102-91de-92777af7c0d9",
#     # States w/ 2 congressional districts: duplicated 07-16-23
#     "ID": "ab09bc34-c83d-4327-9b59-c53c71682151",
#     "MT": "d7fd9cdb-4677-47b0-930a-f53f6b044b8f",
#     "NH": "8624cdac-7fd1-40ca-a47f-c196f8a84df7",
#     "RI": "ee4cfa0f-930b-4f74-9adc-e3b4fc939a63",
#     "WV": "8b2f8ec2-1d12-468a-b445-11c9f6097f74",
# }  # Duplicated 11-16-22 (except for states w/ 2 congressional districts)

# # notable maps for 42 states with 2 or congressional districts (except HI and ME -- see above)
# # Pulled 11/07/2022 (except for states w/ 2 congressional districts)
# # These were the *reported* notable maps. We used a few different ones for the analysis.
# notable_maps: dict[str, dict] = {
#     "AL": {
#         "proportional": "5d573512-b4c2-4f6f-ae2d-c922a10f44fb",
#         "competitive": "3cd2a04e-cd87-40f5-a94f-6bdea8949c0d",
#         "minority": "5d573512-b4c2-4f6f-ae2d-c922a10f44fb",
#         "compact": "9a0a4eb9-8be2-4166-a58c-3df2847b9a52",
#         "splitting": "9b7f6d4e-2afe-40c1-853f-4bbad07f9263",
#     },
#     "AZ": {
#         "proportional": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
#         "competitive": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
#         "minority": "e5491bb3-b05d-449c-936d-0f3bdcadd2cd",
#         "compact": "13e2724a-cb3c-4751-92f6-c8f0476ea6bb",
#         "splitting": "11c9e5f4-b0bb-402a-aec9-f3104d80c443",
#     },
#     "AR": {
#         "proportional": "22bd6016-ba50-4e4c-90bb-2711d589ba1f",
#         "competitive": "719ae353-37dc-47ad-9c16-fc83451542a4",
#         "minority": "20ee252a-a679-4a7d-8075-26f660699ab7",
#         "compact": "fe847577-e642-48c7-9582-8eb23a959275",
#         "splitting": "bf1ef1c3-56c9-4f31-9b07-0be1bbc1289e",
#     },
#     "CA": {
#         "proportional": "04e6b230-5a5d-4e0c-b4f4-a49b331096a8",
#         "competitive": "253d0168-5863-4991-856e-983c8676a1b5",
#         "minority": "b79d4e43-2fc4-42cd-8370-de163c320368",
#         "compact": "4bba5cca-2c5e-42d9-a49f-95f48e311f7c",
#         "splitting": "774a680c-ad29-43d5-af16-6b9c6cc2f17f",
#     },
#     "CO": {
#         "proportional": "8bdb3895-3b9a-4460-bbb9-c9888711a7c7",
#         "competitive": "6f696afa-73e7-4ff4-8407-c4386d65ebd2",
#         "minority": "28f40e7d-b056-4170-8337-ec92c596d572",
#         "compact": "af01f470-753a-4247-862f-eeeb12604ec7",
#         "splitting": "a78ca039-b9af-4816-ae03-6f842f3cab9c",
#     },
#     "CT": {
#         "proportional": "7af97d6e-144a-4183-a83d-0dff2def50c2",
#         "competitive": "7408228f-adfb-49b9-bf1a-28c754e7e413",
#         "minority": "3d23b022-0589-404f-ab51-a75df5bd13e9",
#         "compact": "9e314327-f2a7-4788-b415-1a55d0c3486e",
#         "splitting": "e0cd942f-ee7f-40c0-a641-50ba23e08989",
#     },
#     "FL": {
#         "proportional": "f9978e47-3746-4ae3-bc93-d634b3c0078c",
#         "competitive": "77807f2e-5fbc-4b4c-93f4-078be63ab5ec",
#         "minority": "01131b32-fe72-4572-aaef-696387136286",
#         "compact": "f9978e47-3746-4ae3-bc93-d634b3c0078c",
#         "splitting": "67d684eb-bcc9-4ca3-935d-ea7b77fdc8ba",
#     },
#     "GA": {
#         "proportional": "4a96b0c9-ad11-4b64-aed1-314c09310438",
#         "competitive": "db0689d4-7a77-4df5-a335-a57af2ed1da7",
#         "minority": "682301e4-14b1-486a-a6b0-feac1c07670e",
#         "compact": "a95a3daf-8eec-46ac-8454-c9b829e325c7",
#         "splitting": "4a96b0c9-ad11-4b64-aed1-314c09310438",
#     },
#     "IL": {
#         "proportional": "cbad09de-f1de-49da-95ff-1a6553d3d0e3",
#         "competitive": "94f6e3fe-3f21-44eb-9321-dc2523a88ac3",
#         "minority": "26977538-7b78-4dbf-95e0-28afc3ea7803",
#         "compact": "cbb62424-78af-4dd8-811c-b9563ad59189",
#         "splitting": "5fa6ed67-07a4-411a-a8a5-42920f367d84",
#     },
#     "IN": {
#         "proportional": "6818af19-93ab-4f84-b25e-5248f6dccab6",
#         "competitive": "e4c89f1e-3255-41a1-8e5d-0b587a8d2f52",
#         "minority": "8bab38bd-cacb-4c6f-8dd2-21d359053176",
#         "compact": "b80fc5ee-4642-4bd0-b60c-a3f0c485d765",
#         "splitting": "b10f29da-ce52-4d2b-8c2e-39def8204419",
#     },
#     "IA": {
#         "proportional": "237a6d9a-67b6-40c5-8b93-bbf0f39b53f9",
#         "competitive": "49beb7b3-4328-45b0-ba46-1336e085180a",
#         "minority": "d8b1efb6-089b-4059-bbd7-44d6cb4ad3e0",
#         "compact": "848416dd-0b95-43e7-b6e5-47e896dd7565",
#         "splitting": "2fd0aa0c-91fa-4239-8faf-936e300ab19e",
#     },
#     "KS": {
#         "proportional": "cb7003a3-fc41-48db-b9cc-6c0c5afdb018",
#         "competitive": "58741a3c-7777-4a4d-82bd-5d8252f37ae6",
#         "minority": "b031e66b-4fd6-4b36-901a-5f857468fc6a",
#         "compact": "df9a2ac9-be16-4380-9815-ae6a4ed4773a",
#         "splitting": "b8e49933-96d2-4c80-a5f2-33e804a1ab57",
#     },
#     "KY": {
#         "proportional": "4f0b4319-f1aa-4e8e-b55c-3100719974ec",
#         "competitive": "2086785f-93e8-4268-9c7d-e3b60ddbf666",
#         "minority": "eb314eae-f4e6-4b50-ba5e-5d77174dc0ec",
#         "compact": "3a541d7a-192a-451d-a8bf-e01687292adb",
#         "splitting": "ed7c4e05-3c95-4e89-b844-8a0f231ff195",
#     },
#     "LA": {
#         "proportional": "312c0078-4688-4421-a6c7-c9751ded611f",
#         "competitive": "48d5f83f-c070-4783-9893-d8bf889f095e",
#         "minority": "312c0078-4688-4421-a6c7-c9751ded611f",
#         "compact": "d3a27a1b-82f9-4749-ab09-7a2d1b563f02",
#         "splitting": "1183a889-beae-45dd-81bf-96ffd1256ce2",
#     },
#     "MD": {
#         "proportional": "e3e93c31-764c-4ce3-9bdc-6ee3c945df9a",
#         "competitive": "e3e93c31-764c-4ce3-9bdc-6ee3c945df9a",
#         "minority": "d8dc1ebe-058c-403a-926a-e5bd560369b4",
#         "compact": "2a9b5438-2740-4980-918e-099050b3df94",
#         "splitting": "70801f37-715e-4e7c-b203-c7789c244d4c",
#     },
#     "MA": {
#         "proportional": "20f6aa40-ceb3-42a2-9d03-a6139efa3471",
#         "competitive": "2bdbac0c-b6bc-4183-b160-52f019046447",
#         "minority": "1dbadcc4-a0c2-42b0-863d-d5b54a44ced8",
#         "compact": "af6430dc-008a-4d39-ad0a-c84bb2ffaa79",
#         "splitting": "fffc7551-b217-43b3-86aa-0875c76f4549",
#     },
#     "MI": {
#         "proportional": "517c0e1c-0e6d-4dc5-900c-8e15d6a65d23",
#         "competitive": "63d3e83b-7e54-4e4d-81b0-9d2160c9a1dd",
#         "minority": "c4cf8435-4c0f-4b59-b8ec-f74e593301a3",
#         "compact": "19e6a5c0-25d7-4780-a95f-585ef0fb21cf",
#         "splitting": "20a791e1-051c-4a25-a7a2-c38278c8dc71",
#     },
#     "MN": {
#         "proportional": "a5322380-f9a1-40e7-a541-8f5ae2b5973f",
#         "competitive": "190e7e43-3bb3-4373-93bd-defb9a1a783d",
#         "minority": "e87547ac-3fe1-4dd5-8249-2736ab4616b7",
#         "compact": "b66771be-1286-4b2c-928d-01337995c336",
#         "splitting": "c168bd72-3e9f-4aa9-accb-703055567490",
#     },
#     "MS": {
#         "proportional": "30887944-655c-4acc-a2e9-1e0c4b78137c",
#         "competitive": "3aee6676-fb1f-45a2-a27d-11efa8072d48",
#         "minority": "f2c96cf7-9c23-449e-81c2-72b8aaf388f3",
#         "compact": "4fc7f506-0993-47ea-8459-37f89d326c25",
#         "splitting": "592e3a73-cac8-4f00-a507-e339b44ad092",
#     },
#     "MO": {
#         "proportional": "5f18a76c-f3ad-4ba1-8d50-1db6cec56f1f",
#         "competitive": "5830b5c8-fb14-4af5-8acc-ec3dd27f448c",
#         "minority": "d393f212-17c6-4de0-bf03-8afd288c5234",
#         "compact": "35607bfd-2363-421b-8a0e-ec8252bcc4f0",
#         "splitting": "189d6bd7-27fc-46bb-b4a7-93dc96dad09f",
#     },
#     "NE": {
#         "proportional": "fad7dd6a-b3fb-44a2-b159-6634efd1a4b6",
#         "competitive": "f9e38118-22d8-4493-a12d-509b7711324a",
#         "minority": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
#         "compact": "d1f97366-8fb9-489a-a11c-a0b1ac10673b",
#         "splitting": "e3f66393-18fc-4d37-9599-32411ad2bf20",
#     },
#     "NV": {
#         "proportional": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
#         "competitive": "ad048a79-af54-4092-aa8f-f14a0947df4d",
#         "minority": "cd1c643b-7353-4d8e-b9ab-072ef603508d",
#         "compact": "628a65f3-abf3-412b-9ef6-7cd20bfeac73",
#         "splitting": "7b4f4269-1c31-4fa8-a282-cd8f1fa3b5e6",
#     },
#     "NJ": {
#         "proportional": "be03805c-45c0-4bbd-8760-dc738705bcde",
#         "competitive": "535e013f-5db5-4a9c-9edc-496d65972781",
#         "minority": "1f2e6cb7-61aa-4a8b-8800-38ce8a767248",
#         "compact": "6fcb6b8b-2565-4831-990f-b978b88cc253",
#         "splitting": "c24cf3a7-541a-472a-9e3f-6ebe398e8c33",
#     },
#     "NM": {
#         "proportional": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
#         "competitive": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
#         "minority": "b3946cfb-7567-46a1-9fc5-6a226db7728d",
#         "compact": "714b1ebf-9280-463a-b02e-e1781196dd3a",
#         "splitting": "3cab7943-cc5d-4c56-a460-307ca987324a",
#     },
#     "NY": {
#         "proportional": "4185458d-6708-42ad-902c-ae9f9eb832bc",
#         "competitive": "e8fcc5ee-9151-4ef8-9ef5-66fb80be9317",
#         "minority": "fe733d47-6219-48ad-9a61-3a3933da7e61",
#         "compact": "59761137-e122-48ff-980f-9538074360c8",
#         "splitting": "72b69a87-0f16-4963-95a8-9d210bf14fb5",
#     },
#     "NC": {
#         "proportional": "7cfcec86-b8bf-41fa-a6c2-0be9b3799747",
#         "competitive": "40178c75-312d-4789-a457-d609b0d8a043",
#         "minority": "3b168396-6666-4167-830e-4500bde459fe",
#         "compact": "3bacb15d-e014-4764-9e8c-f238eb687d50",
#         "splitting": "82e6303c-e842-469b-b364-918bcacf9ef3",
#     },
#     "OH": {
#         "proportional": "c609d0a3-d838-4d92-b40b-f706a3e616f4",
#         "competitive": "eb5ada10-d1d7-43c5-b02a-4c969bc5e5a2",
#         "minority": "72489412-c5ba-4d8a-8f77-dad9e9a596f4",
#         "compact": "c609d0a3-d838-4d92-b40b-f706a3e616f4",
#         "splitting": "e8c64e09-f406-47a2-921b-eb08c1020803",
#     },
#     "OK": {
#         "proportional": "8571df5b-1648-4465-8d00-5e0b36cd75c0",
#         "competitive": "8d4d5241-fc6f-4c7d-b953-f5f7e0071e6d",
#         "minority": "c42edda8-9784-4c3e-ad11-ba3512ee0845",
#         "compact": "5d052539-7560-4200-9e96-c920cda86b4f",
#         "splitting": "3dbef3e8-e5ff-4d81-8d81-cb4c55892461",
#     },
#     "OR": {
#         "proportional": "409bed65-c9a0-452e-8b68-1f4f0b1dc67e",
#         "competitive": "c73a3d8b-3648-4488-a6ce-cfd512f2c6b6",
#         "minority": "bedb8c6a-5661-4cfc-ae59-6e51dd9d63d4",
#         "compact": "b9215af6-e56d-4bd7-a414-75086e0e96eb",
#         "splitting": "3eaf150c-fc28-4d24-b15e-606a5253e9d4",
#     },
#     "PA": {
#         "proportional": "b1f9190b-4c0b-4c9d-a8f9-64d296c040fe",
#         "competitive": "d88bcad5-2aea-462f-af79-269a0c85db19",
#         "minority": "7e00b136-2831-42d4-a455-060a94e0af77",
#         "compact": "8a2a7dac-1c36-47d4-91fb-3147fcb5e6dd",
#         "splitting": "da43a46c-1ca4-41ab-acd2-e07ceff538fd",
#     },
#     "SC": {
#         "proportional": "56fc8132-911f-4dc8-a624-405e65ed33af",
#         "competitive": "3cd7600e-7a08-47b5-8175-252b70ce38ea",
#         "minority": "71866f45-008e-4891-9a8b-b24763205725",
#         "compact": "cb454bbb-950b-41c9-8d9e-0cba47e0c6ea",
#         "splitting": "14fb2ae8-9e79-45d9-8492-30c07511a107",
#     },
#     "TN": {
#         "proportional": "bb2bde21-934e-484b-90b5-496eb9bfbd44",
#         "competitive": "a8d8ab31-92a8-4b7c-871e-91241c235b9e",
#         "minority": "47a81f0b-4bc0-4069-a9f4-cd3c948a6ebd",
#         "compact": "993cde69-8adf-4fef-8b90-475f8d525810",
#         "splitting": "a94ff5a0-9d8a-4234-8a02-7ae698a2741a",
#     },
#     "TX": {
#         "proportional": "9b000c6e-f8f5-4d50-b060-81f9c8ec8d21",
#         "competitive": "ac91c9a3-331d-4b23-b2f5-8d5ca11e8e25",
#         "minority": "a2120eda-e2ff-47d0-a06d-d8305eedd227",
#         "compact": "ea165cec-8fd7-4c1e-854f-ecc789416873",
#         "splitting": "a89fe1b1-7a37-4654-91bf-f6ac2c8fe661",
#     },
#     "UT": {
#         "proportional": "5c881c02-483b-4df8-bfd1-c32486e31138",
#         "competitive": "8c187e06-a4f8-4778-9ccc-d237ffc6f091",
#         "minority": "1593ee86-9176-4e92-96b5-6f801f3e13e4",
#         "compact": "5c881c02-483b-4df8-bfd1-c32486e31138",
#         "splitting": "5c881c02-483b-4df8-bfd1-c32486e31138",
#     },
#     "VA": {
#         "proportional": "31607948-2ad0-4e68-a8ce-e175fcfc3ddf",
#         "competitive": "22700e82-9423-4029-b94a-78ebb16dc962",
#         "minority": "479fcea5-a312-47bb-ba2d-377f3cbd1ea9",
#         "compact": "55426dbf-1d87-45ce-b164-77d8ae985898",
#         "splitting": "a0402468-c3cd-4858-b72d-a37eecb4ca16",
#     },
#     "WA": {
#         "proportional": "7e3df196-530d-474d-85d2-12db2b865609",
#         "competitive": "d544f633-89a5-4b8e-9080-d693bd527475",
#         "minority": "7b82c987-3779-49c3-b1b8-df838580c9aa",
#         "compact": "cab3e806-3015-4e65-8daa-d5267f949046",
#         "splitting": "780082a2-bd41-4787-b18f-bfaf31fe8739",
#     },
#     "WI": {
#         "proportional": "2b2705c6-7532-40eb-8521-af8bdc66de25",
#         "competitive": "2786ff99-aead-4585-9246-ce2dbc5bcc47",
#         "minority": "1943dc12-a393-4b9f-a688-cd5365e208f4",
#         "compact": "b6942ec8-9615-4e6a-bdbd-275b196a840f",
#         "splitting": "bc908f90-e0ad-4e92-8514-512cebebb637",
#     },
#     # States w/ 2 congressional districts
#     "ID": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "competitive": "53a1b547-3a7e-4fe7-ab58-7badc6274e6b",  # 07-16-23
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "compact": "206912f7-878a-4f21-b188-f40320ab558d",  # 07-16-23
#         "splitting": "abd274f0-847c-4c53-934e-646c84d81aac",  # 07-16-23
#     },
#     "MT": {
#         "proportional": "0c96f1a2-d4c9-4294-b2d4-a20aa9d2b04d",  # 07-16-23
#         "competitive": "e1058b7d-1cca-46a0-98ec-d95dd3d353a1",  # 07-16-23
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "compact": "7838e111-d287-43c5-97ac-d04366cb6d1c",  # 07-16-23
#         "splitting": "a50422e4-5596-4385-808b-7bf0639b5d63",  # 07-16-23
#     },
#     "NH": {
#         "proportional": "c180d0a8-cd75-492e-9fe4-98cf3df931d1",  # 07-16-23
#         "competitive": "adce2bd3-8f35-4437-9dd5-86bb5e1864b1",  # 07-16-23
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "compact": "3ed6cd29-1807-4a82-a4e8-c6512d28ab77",  # 07-16-23
#         "splitting": "5fc07325-9519-4bfb-9279-6701e9026af1",  # 07-16-23
#     },
#     "RI": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "competitive": "f4a1138f-fe7e-4127-bd76-d2cb718d3bfb",  # 07-16-23
#         "minority": "ffddb68e-700a-4d85-85f5-edfe061ec821",  # 07-16-23
#         "compact": "344ecc9b-b641-44e7-87b2-1ffd6d69da87",  # 07-16-23
#         "splitting": "344ecc9b-b641-44e7-87b2-1ffd6d69da87",  # 07-16-23
#     },
#     "WV": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "competitive": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  # N/A
#         "compact": "b497117a-9d00-471e-9d1a-b69ae960c48d",  # 07-16-23
#         "splitting": "5e630f86-6a48-4942-b613-51d4c572af93",  # 07-16-23
#     },
# }

# notables_copy: dict[str, dict] = {
#     "AL": {
#         "proportional": "e9851c4d-2b32-4da0-adaf-86762af78e26",
#         "competitive": "9f3cd446-144f-4824-9ce2-3f6d52ebf74c",
#         "minority": "14942ba2-c86f-4e7b-a1e7-51d7f243dd84",
#         "compact": "b556aea8-e259-40e1-9b29-4e7572d6cbae",
#         "splitting": "94c7b2b9-f8d0-4d89-aae1-53cfd9009f97",
#     },
#     "AZ": {
#         "proportional": "318578e0-ae95-4319-aa7a-34838c016cdd",
#         "competitive": "17345788-c122-43be-a62a-5c43a696a22c",
#         "minority": "5b4dfad5-ee34-469d-bdef-7f07a749b2c5",
#         "compact": "970224ba-4373-48fd-9e3e-15527b63c9c5",
#         "splitting": "7ff7eec5-1b01-422b-bb34-d78da0f8fcb8",  # copy of "2dff53e3-4c0a-499b-b3c9-26e409318e83"
#         # "splitting": "01aecc9a-2a4b-4d43-9ca7-96385c0d1daa",
#     },
#     "AR": {
#         "proportional": "4331cceb-5317-4921-a620-1197799add51",
#         "competitive": "9ff90f72-33bb-4d70-a7d6-91fb30502bf8",
#         "minority": "d6e55da9-dd51-4429-ba40-78bbfe3105e4",
#         "compact": "c53002fd-1f4e-4f3f-86c8-00e738d7cbe5",
#         "splitting": "ea810d0f-a507-416e-a0f6-58adbf93df6e",
#     },
#     "CA": {
#         "proportional": "e2b59dd7-629e-4856-9f35-b37751ee101e",
#         "competitive": "ade2f538-fe9b-4e37-9a7e-d9c87ea717d5",
#         "minority": "07cd471f-0ebc-449e-ad7f-534ec8d9e78d",
#         "compact": "42bf9029-6e68-481a-be75-a1f339248cba",
#         "splitting": "fbefc34b-ac86-4081-8731-b731d95e67f9",
#     },
#     "CO": {
#         "proportional": "69886296-e646-4bb8-841f-40faf888463e",
#         "competitive": "d11c4b86-1f01-4adb-8b70-7d17d640de46",
#         "minority": "2427fc2b-4907-4fac-a1fd-54fe225db227",
#         "compact": "e9e9c486-bb80-4ce5-9666-4466947f7ab0",  # copy of "7d34443b-3e8c-4108-9074-2e565805b89d"
#         # "compact": "5970deaa-8306-4728-8933-3a74d1f2f298",
#         "splitting": "d639dbaf-cf30-4998-b794-7cfba3312a0b",  # copy of "fe586498-24d8-4c7c-a6db-8437ed0b9ca6"
#         # "splitting": "896e564c-ddfa-4596-9c3d-a6dbd9b6e886",
#     },
#     "CT": {
#         "proportional": "6411d3ac-8523-44b2-a9e1-4abc0469790c",
#         "competitive": "b10fcc44-6db9-435f-bd37-f1b8524e32b2",
#         "minority": "2ce70cfc-ab32-48eb-a485-7d33bd201ff0",
#         "compact": "d8e5dbfd-c7b1-48a9-a3ee-c606867acfe7",
#         "splitting": "76865f59-03ed-4647-95a2-c6d64a7b9270",
#     },
#     "FL": {
#         "proportional": "6ba89c54-906b-4753-85d1-c82caff8a597",
#         "competitive": "19f48062-920f-4659-bcad-9b7b10b7a150",
#         "minority": "9191dc5d-fef4-4920-825d-c1b29f842dc7",
#         "compact": "35789bfa-b77d-4a42-a86d-5ce161d24514",
#         "splitting": "94248293-2880-49b1-9dc3-cb8ff77f3e58",
#     },
#     "GA": {
#         "proportional": "0f6d64be-4cdc-457e-8712-90514e74de9b",
#         "competitive": "d83f0a86-bea5-4728-869b-207072f53bb3",
#         "minority": "f3527d3c-41b5-4758-8560-6ba52695c3b8",
#         "compact": "daec754f-45d0-43d3-bdbf-e8637e7cfe8d",
#         "splitting": "bf30be3a-0924-4790-a353-83ca0152504a",
#     },
#     "IL": {
#         "proportional": "0764d8de-7366-4572-8617-cdf5f00bbcbc",
#         "competitive": "6e6ecb9a-2385-4b40-a0ce-b2217ce92c47",
#         "minority": "0d4b32d4-bf9d-41a1-b15e-807daf0cc128",
#         "compact": "6ff3964a-0009-4cc0-a643-0f8f9b2096b8",
#         "splitting": "0cfac142-a509-447c-95a7-77c3b87d467d",
#     },
#     "IN": {
#         "proportional": "1f6ff4fa-53ed-499a-81e7-cd80296c6946",
#         "competitive": "ee9ba611-992d-4c0f-b947-80979f23e38e",  # copy of ???
#         "minority": "101f80a9-cfc0-423b-b0d6-29e81403b46c",
#         "compact": "f59e9631-2abe-4753-bc3a-b9a5186d233c",
#         "splitting": "07f032b2-ec89-4bde-8ec5-57224285172c",
#     },
#     "IA": {
#         "proportional": "b8cff1b2-059a-421c-92f1-168eecb0860d",
#         "competitive": "a62a4544-8ab9-4641-849c-ab9f68e842bc",
#         "minority": "d6e9ebe5-9e71-4e1d-adad-584868220635",
#         "compact": "3888d170-52fe-44fb-8428-d0e08b8cdcf5",
#         "splitting": "311d779b-9cfc-4983-a589-a9d6877e3f1e",
#     },
#     "KS": {
#         "proportional": "177278c7-822b-414c-a6e4-47c49e6d8e31",  # copy of "5e0fe356-4f7f-49eb-b36b-693b1a156845"
#         # "proportional": "659e9adf-713c-4375-9528-f384d043f1b0",
#         "competitive": "cadda27c-9616-45b6-a872-2d5a6e60c6a1",  # copy of dfabfef9-429c-4b81-a893-da79e7e26214
#         # "competitive": "e2021c4b-281c-451a-ad9e-49fef9c2f57b",
#         "minority": "5e4b3a7d-cb16-4cee-ac4b-05086203c64d",
#         "compact": "d86bf787-674a-4a6e-8cb8-e84c45762077",
#         "splitting": "7ac2a17a-c287-41ff-b624-67efe0bea826",
#     },
#     "KY": {
#         "proportional": "da1a0bdd-7f3d-43e4-892e-b1c111b46d4d",
#         "competitive": "5c8fe427-5ca5-4168-a225-7c510aa85ef1",
#         "minority": "036aeb13-a3c3-4ef6-8be8-5af7bab6b730",
#         "compact": "424d91c3-a26e-4083-8790-06f8384d2c44",
#         "splitting": "37c63cb2-3bec-418f-8fee-c841ddc5e3c1",
#     },
#     "LA": {
#         "proportional": "38b5cae0-cc85-4eb7-aa0a-ff1cfd3db549",
#         "competitive": "cc002cfc-68a1-4884-9cf1-f9a33c9b1add",
#         "minority": "0be18b01-7044-4055-8de8-596a2cae3039",
#         "compact": "fcc9a519-3aaa-4003-84cf-9807ec8bad4a",
#         "splitting": "02689947-7712-4139-aa39-2e5ea6add817",
#     },
#     "MD": {
#         "proportional": "55459ef3-26a1-421a-9267-d7a113c306dc",
#         "competitive": "f98eba6b-5297-47d1-bc38-9d5548077fe7",
#         "minority": "af482991-ee6c-4180-8782-57f667a55919",
#         "compact": "530f41fb-d39f-492a-9028-8886bd499eed",
#         "splitting": "d26ec0e1-f53a-4ebd-9aa8-7e18accb04af",
#     },
#     "MA": {
#         "proportional": "b9eff778-303e-49ec-a4f0-a0165a05a665",  # copy of b9eff778-303e-49ec-a4f0-a0165a05a665
#         "competitive": "7cda7048-7362-4543-998a-2c1b89de88a8",
#         "minority": "6fdf3a89-1b63-4856-bcbb-d777b01f51a2",
#         "compact": "ff5a5d69-1c81-4ce2-927b-ddb010968b33",
#         "splitting": "6e745232-b017-47de-b20a-09de51e720f1",
#     },
#     "MI": {
#         "proportional": "4c1a46f3-3eed-4b0b-9f1e-74e1e1c63a97",
#         "competitive": "fd5de4ef-5069-4aa3-987e-0c4faa50f9d9",
#         "minority": "2d2c9c5a-8812-408b-9343-36317052bd95",
#         "compact": "6a943e97-c4d7-4111-939a-6eef1fb652d8",
#         "splitting": "b0c02efc-6507-4e73-93c2-1ced3d8d469f",
#     },
#     "MN": {
#         "proportional": "e96c7448-d5ba-4500-b158-06f2ff6e1453",
#         "competitive": "7e2f65af-b848-4ecc-83d3-f0e958b9406f",
#         "minority": "fcfc1a01-7ad3-46c3-a3e6-41222ea0cf48",
#         "compact": "64858a6b-6511-4f16-834f-776ab91205e0",
#         "splitting": "1d7a0cc7-7199-42a8-805d-8f7e14c60d6e",
#     },
#     "MS": {
#         "proportional": "78f2536f-c30f-41f0-ace3-d0f2597f7c27",
#         "competitive": "e7be9ef9-d9ff-42ca-8e04-3226b3b413d8",
#         "minority": "cf2ebd05-d118-4ecf-a8f4-824c6cb6ba67",
#         "compact": "9e1d67b8-162c-4c44-b15a-263d3ae6f026",
#         "splitting": "35c56e88-6ac3-4f3e-b732-7e37221395c7",
#     },
#     "MO": {
#         "proportional": "a39beb81-f839-4755-a35f-05bc79ee68a0",
#         "competitive": "f07502f1-f94d-47c6-b083-f41aadb0f7ee",  # copy of "127dfd4d-094a-4cdc-ac9e-e98829a664dc"
#         # "competitive": "a110a70b-d083-4934-905c-2ba0dae7256f",
#         "minority": "d1ce2e50-1c28-4aae-a95e-71b1ab361c8a",
#         "compact": "9cc3d9c3-44c6-4a62-8db9-7846ac12688f",
#         "splitting": "abc98af0-3ef8-4861-96cc-40f7173d9d14",
#     },
#     "NE": {
#         "proportional": "a2d83af8-8aab-492f-9f10-9be4b9a263f1",
#         This next map is bad! 2x number of districts
#         "competitive": "64d87e1d-766e-4907-9324-bfec457e1711",  # copy of "c15b16b9-65f9-4814-9958-1aeec10d3ab0"
#         Replaced w/ "f9e38118-22d8-4493-a12d-509b7711324a"
#         "minority": "eb4be8c9-3ea4-494f-a98d-226f597bd5da",
#         "compact": "f7720b75-58d6-4e2d-bff0-894e2c7b5f41",
#         "splitting": "4ff0b106-818d-4f7a-987a-39205bdcb008",
#     },
#     "NV": {
#         "proportional": "c9b38b70-d05a-4d6f-b6ec-f237da8ca34f",
#         "competitive": "3ac3a189-ea62-4d90-baec-6e7e46c9893d",
#         "minority": "387a0b00-171b-4821-8479-63bcdaf2d79a",  # copy of cd1c643b-7353-4d8e-b9ab-072ef603508d
#         "compact": "8da2d779-b8bd-4e27-bae7-340fa87a4376",
#         "splitting": "baa3cfad-e4f8-452c-9c5d-a71bd4efd9ff",
#     },
#     "NJ": {
#         "proportional": "5cb13428-1e13-4e5e-b4ab-547478caed4b",
#         "competitive": "3c54c696-ae75-4eda-a260-5a95a2c276ef",
#         "minority": "7a67aa4f-a75a-4958-9d91-ae6cdbf91d80",  # copy of b794c93f-5033-4c36-bd93-1a93b48de442
#         "compact": "f254884d-267e-43b4-9d7e-2d9812c13788",
#         "splitting": "a3afe5ca-4430-483f-82ca-39922fa5d3dc",
#     },
#     "NM": {
#         "proportional": "2051bf23-0195-4d89-aceb-252d78c32dc4",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
#         # "proportional": "1739a3fd-0a61-40b4-affe-2d9943568477",
#         "competitive": "57893e66-fd7d-464a-8e6f-c39b69609b73",  # copy of "0852f3ca-438e-43be-858c-72e6fd797f98"
#         # "competitive": "2e487b62-e26b-4c96-92de-0ffd20feade6",
#         "minority": "46afff6c-1f2c-43bb-bfeb-1c69f75fa403",  # copy of "3cab7943-cc5d-4c56-a460-307ca987324a"
#         # "minority": "5dcbf4ee-ad06-4fb2-9d30-45b7b1496a3f",
#         "compact": "769b245f-4c5d-4a93-98a5-6cd2e66420a2",  # copy of "e7ac5c2a-ce36-4780-ab04-0fc82faac874"
#         # "compact": "a569b54b-eebb-42c7-af2a-373d13142d05",
#         "splitting": "cd28107e-5ede-4f74-bbf5-dae7f54c17e3",
#     },
#     "NY": {
#         "proportional": "65aaf6b6-2abf-4f2f-9313-7fb0c32aca2c",
#         "competitive": "48987808-7ab5-4846-b281-54f58bd24d67",
#         "minority": "20775253-b960-4542-8a7b-165635b006cc",
#         "compact": "6d9a1e16-c5d2-48a0-80f1-d06fe6d56b7f",
#         "splitting": "149fe85d-04c2-4d11-b959-98fe52f1772b",
#     },
#     "NC": {
#         "proportional": "eb89e54f-69aa-4742-90e9-83b696871348",
#         "competitive": "3ba3e193-414c-4a17-a9ef-57b326ede3d9",
#         "minority": "565513d2-f7e5-492f-81f7-7cd10c054a18",
#         "compact": "c9ed708a-3c2f-4b29-b55e-3bbfda14db7f",
#         "splitting": "fbbde7c8-f8e6-47ff-ae18-8307f344a8f6",
#     },
#     "OH": {
#         "proportional": "43ac2051-66af-46d4-817f-3fca031b4008",
#         "competitive": "e7043d87-a24a-41fd-b3e3-f4a1162548a7",
#         "minority": "b95bb90a-426f-40a0-a06d-d3027e646617",
#         "compact": "486a1fd0-f56e-435b-8e69-a080e99fe58d",
#         "splitting": "5c6e887d-49a8-426f-8b7b-5f3400cc62a1",
#     },
#     "OK": {
#         "proportional": "2943140f-a1bd-45c1-a455-dc14c5393eed",
#         "competitive": "ca3b3e26-9a73-422f-a40c-cd7b240e053d",  # copy of "2de2dd82-508d-4c6d-a626-b41373f1a9b7"
#         # "competitive": "b8794457-352e-4412-9908-027f95cc9b1d",
#         "minority": "9d2fa2d3-a6fa-4b65-b902-3d26e8c7b41a",
#         "compact": "fbec07f7-2c67-4928-aedc-956f551aee08",  # copy of "10e4bc47-38a4-4b0d-9329-81b40bc039f4"
#         # "compact": "5d052539-7560-4200-9e96-c920cda86b4f",
#         "splitting": "d47c3741-ec79-48d4-8c95-f938a526cf4b",
#     },
#     "OR": {
#         "proportional": "49749f47-8d78-4d36-a8b3-1265cd3b0191",
#         "competitive": "37764638-8e2d-45d0-8322-28c4a171d71c",
#         "minority": "b914939e-5e90-4e73-a51b-60e157670b24",
#         "compact": "6d9ec3b7-e462-401f-ac5b-9ef37b35f32e",
#         "splitting": "6a9fdbbb-01ce-4a5d-8fcb-38788646368b",
#     },
#     "PA": {
#         "proportional": "60f36296-fdbc-420c-9094-91efbe53041e",
#         "competitive": "e3c3b909-508a-4095-8c22-93ba9fc5b030",
#         "minority": "17290afc-2e93-407b-af6c-c6a26d051dad",
#         "compact": "e0fa7e79-26a4-4d27-8028-745a84fea1c1",
#         "splitting": "dc16b2ec-4609-42ca-9ea8-02697564d52c",
#     },
#     "SC": {
#         "proportional": "5132f119-2ca1-4b91-9c67-9517ae1824be",
#         "competitive": "521725a2-3c2a-498a-bb95-0a64622b5d52",
#         "minority": "206ddd70-ef2d-48ff-ba91-c7db687cb9a6",
#         "compact": "bf225fbb-c06b-4a26-a00c-e98bd9344347",
#         "splitting": "31408783-0ca1-4c94-abf4-20270ef87c22",  # copy of "46a975e5-30b4-4277-9dbc-2609b452eaa2"
#     },
#     "TN": {
#         "proportional": "c9ec1171-e733-41be-ae73-faadbd4f9eff",
#         "competitive": "b44dbb99-35d6-4a09-97ec-0f0654bb0d83",  # copy of ba9b21a7-da1f-46cc-ac5e-11b12215268d
#         "minority": "c0c61d14-db2e-44db-8b81-c9f535808b3a",
#         "compact": "57c3bb60-5f54-4cc1-a1b7-4942584fdc6f",
#         "splitting": "812ca788-8a2c-4300-ab53-3979518f16bb",  # copy of 32587b8e-f18b-463f-8f30-86a3fdbb8bd7
#     },
#     "TX": {
#         "proportional": "5a8bcd01-5b7b-4cb0-ba97-775c127412c2",
#         "competitive": "b3168e80-5ec4-49e2-b3bd-928cf2ffffdc",
#         "minority": "55687012-5c38-4fc2-9b19-a6b325e5e8cb",
#         "compact": "3670b0b1-7083-4d20-9cee-5c5389dfdcf4",
#         "splitting": "959c211a-e7db-40fe-9703-0082de3fd50f",
#     },
#     "UT": {
#         "proportional": "cb2cd60d-74db-41a4-bcd3-d2908033a17a",
#         "competitive": "29776f42-efdb-485d-942d-9ec738756de9",
#         "minority": "0c38f235-f832-43a6-b77d-98ffcc4a196f",
#         "compact": "d4b7682f-e1df-40d0-9770-6d85a1176a12",
#         "splitting": "a26f10a5-cfeb-4989-919c-5df3c79dcb29",
#     },
#     "VA": {
#         "proportional": "e629d89d-0ba5-4cfb-af0d-1f5a26540847",
#         "competitive": "b2e40a2b-d0c3-4394-bd6c-9a387977d577",
#         "minority": "3ff32d6a-1ddc-47df-ba3f-d1004f6ec6ab",
#         "compact": "30a7dba3-43b0-4815-8ccd-7abbcfcf5cfa",
#         "splitting": "9bd6b5b4-f8f6-4372-a45f-77b6b1668596",
#     },
#     "WA": {
#         "proportional": "c8ac870c-f608-4f06-a519-fca814cd87c9",
#         "competitive": "ee915375-d42d-4be8-8858-18302b68e684",
#         "minority": "9b6064ae-6aa8-4ea7-af3e-2e0dde3c123f",
#         "compact": "5ece8404-5181-4aef-8dbf-126029f60dad",
#         "splitting": "3a2a23c8-d65c-4a5b-ab4f-35ccb3eab67d",
#     },
#     "WI": {
#         "proportional": "e2a8430d-0721-4a77-a70c-f1b39423f76f",
#         "competitive": "98421457-d1bf-4036-bb54-acf3b87c93c3",
#         "minority": "5af5a6bf-92cd-4467-ad0e-5d513df5f2ed",  # copy of "e8d8bf63-0f1b-4b7b-bb19-f124438a9e79"
#         "compact": "ee9bc88a-f00a-4284-be14-a6b61b9ca203",
#         "splitting": "4ad1f885-3b85-4dc7-bf36-605a122f4b13",
#     },
#     # States w/ 2 congressional districts
#     "ID": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "competitive": "f404dcbc-4763-4405-8ee8-9de38763ab9c",  # copy of "5f1c3e67-1895-4230-80c6-e7d286b6e89e"
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "compact": "c04b3d59-ad9b-4d34-a56c-a40e4a2faaaf",
#         "splitting": "0549f613-9577-4a0f-ba17-f821552e3512",
#     },
#     "MT": {
#         "proportional": "968024a3-66d9-40fb-8503-963475d9ec3a",
#         "competitive": "00899589-f1ed-47be-bed4-2977ad156b5e",
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "compact": "7ef9c6cc-9009-4a46-a135-b02a015e0588",
#         "splitting": "a8bbd540-253e-4c9b-aa51-492925c0a896",
#     },
#     "NH": {
#         "proportional": "9c0a775c-8886-4fcf-852a-c3cd8aad2ff5",  # copy of "7b509654-2390-440b-a022-211cb977b074"
#         "competitive": "4dc15785-8867-4a13-9c06-bb2a7ffecbb7",
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "compact": "7a525a0e-d481-4f1a-a3c7-380134fabd02",
#         "splitting": "fddf7e78-d454-497f-b9a6-d5b5740f21d6",  # copy of "adce2bd3-8f35-4437-9dd5-86bb5e1864b1"
#     },
#     "RI": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "competitive": "9b7b2ce0-e1dc-48fe-89ec-0b2298cdb8f9",  # copy of "40aef9df-2406-4c9b-8e80-b48b273dfd32"
#         "minority": "bd87b715-1286-4ffa-9f42-056f18693d9f",
#         "compact": "56621991-7577-42cf-ae24-8b1cb8fb0587",
#         "splitting": "83816f12-ddf0-4a45-a49d-a9908e2922e1",
#     },
#     "WV": {
#         "proportional": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "competitive": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "minority": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#         "compact": "d0785c40-b290-4c44-9f29-48f28edaf96e",
#         "splitting": "0556f0d1-950d-4581-8777-67cc912d7280",
#     },
# }

### END ###

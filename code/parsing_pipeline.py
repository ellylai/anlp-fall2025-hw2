# 1. html_parser: use links in google doc to scrape for all subpages and pdfs
# parent page and subpage links go in html_links.json
# pdfs go in a folder in pdfs_and_html_links
# use links in html_links.json to convert to plain text (put in a folder)
# 2. pdf_parser: use downloaded pdf files to convert to plain text (put in a folder)
# 3. document chunking
# 4. embedding: sentenceBERT
from parsers.html_parser import parse_html_links
from parsers.pdf_parser import convert_pdf_to_plaintext
from doc_chunking import chunk_documents

def main():
    links = []
    with open("pdfs_and_html_links/html_links_parent.txt", "r", encoding="utf-8") as f:
        for line in f:
            links.append(line.strip("\n"))
    # parse links + html pages
    pdf_links, all_links = parse_html_links(links)
    print(pdf_links)
    # parse pdfs
    convert_pdf_to_plaintext(pdf_links, write=True)
    # chunk docs
    chunk_documents("pdfs_and_html_links/pdfs")
    chunk_documents("../pdfs_and_html_links/html")
    # embed docs + store in vector database
    # pass off to retriever


pdf_links = [
    "https://www.cmu.edu/sites/default/files/documents/UCM-26-911%20CMU_Fact_Sheet_01-MECH-Access.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/4/omb/documents/operating-budgets/2025-operating-budget.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/at-2025-fillable1734728340995.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/24890_at2024_fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/20335_at_2023.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/17011_at_2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/16374_at_2021.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15767_2020_amusment_tax_form.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15768_2019_at_7.25.2019.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/9622_amusement_tax_regulations.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-faqs/et-2025-fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/24891_et2024_fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/20338_et-1_2023.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/17012_et-1_2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15775_et_1-2021.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15774_et_1-2020.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15773_et_1-2019.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15772_et_1-2018.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15771_et_1-2017.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15770_et_1-2016.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15769_et_1-2015.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/9626_payroll_tax_regulations.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/isp-2025-fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/24893_isp2024_fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/20336_isp_2023.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/17013_isp_2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15539_isp_2021.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15538_isp_2020.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15537_isp_2019.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/9623_isp_tax_regulations.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/2/finance/documents/tax-forms/ls-2025-fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/24889_ls24_fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/20340_ls-1_2023.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/17014_ls-1_2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15782_ls1-2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15784_ls1-2020.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15785_ls1-2019.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15786_ls1-2018.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15787_ls1-2017.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15788_ls1-2016.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/9624_local_services_tax_regulations.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/2/finance/documents/tax-forms/pk-2025-fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/24888_pk2024_fillable.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/20339_pt_2023.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/17015_pt_2022.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15790_pt-2021.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15791_pt-2020.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/15792_pt-2019.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/9625_parking_tax_regulations.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/change-in-business-status-form-04.2025.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/taxpayers-bill-of-rights-rev.-06.25.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/16958_2022_tax_rate_by_tax_type.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/16957_2022_tax_due_date_calendar_.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/8271_facility_usage_fee_information_for_performers_and_contracting_parties.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/firesale.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/8398_payroll_expense_tax__et__allocation_schedule_form.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/6825_payroll_expense_tax_allocation_schedule_for_professional_organization_form_instructions8.15.19.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/8397_local_services_tax_ls-1_allocation_schedule_form.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/6822_local_service_tax_allocation_schedule_for_professional_employer_organization_form_instructions8.15.19.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/8403_general_contractor_detail_report.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/tax-forms/7065_general_contractor_detail_report_instructions.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/2/finance/documents/tax-forms/ls-tax-exemption-certificate-2025.pdf",
    "https://www.pittsburghpa.gov/files/assets/city/v/1/finance/documents/6819__lst_refund_form.pdf",
]

if __name__ == "__main__":
    main()

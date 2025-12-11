export interface NavItem {
  label: string;
  href: string;
}

export interface FeatureCardProps {
  title: string;
  description: string;
  icon: React.ReactNode;
  image?: string;
}

export interface StatCardProps {
  label: string;
  value: string;
  trend?: string;
  trendUp?: boolean;
}
